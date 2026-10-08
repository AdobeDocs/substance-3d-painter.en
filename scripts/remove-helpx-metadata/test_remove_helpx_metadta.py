import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from remove_helpx_metadta import main, remove_helpx_metadata


class MetadataTests(unittest.TestCase):
    def test_preserves_unrelated_bytes(self):
        original = (
            b"\xef\xbb\xbf---\r\n"
            b'title: "Example"\r\n'
            b"helpx_url: 'old'\r\n"
            b"helpx_description: text\r\n"
            b"description: caf\xc3\xa9\r\n"
            b"---\r\n\r\n# Body\r\nhelpx_tags: keep this"
        )
        expected = original.replace(b"helpx_url: 'old'\r\n", b"").replace(
            b"helpx_description: text\r\n", b""
        )
        self.assertEqual(remove_helpx_metadata(original), (expected, 2))

    def test_no_metadata_or_no_matching_fields(self):
        for original in (
            b"",
            b"# Body\nhelpx_url: keep\n",
            b"# Body\n\n---\nhelpx_url: keep\n---\n",
            b"---\ntitle: Example\n---\nhelpx_url: keep\n",
        ):
            with self.subTest(original=original):
                self.assertEqual(remove_helpx_metadata(original), (original, 0))

    def test_multiline_and_quoted_fields(self):
        original = (
            b"---\n"
            b'"helpx_description": |\n'
            b"  Multiple lines\n"
            b"  ---\n"
            b"  helpx_text: part of the value\n"
            b"\n"
            b"# Preserve this comment\n"
            b"'helpx_tags':\n"
            b"- first\n"
            b"- second\n"
            b"- name: third\n"
            b"  value: nested list data\n"
            b"helpxExtra: yes\n"
            b"title: Keep\n"
            b"nested:\n"
            b"  helpx_example: Keep nested data\n"
            b"...\nBody\n"
        )
        expected = (
            b"---\n\n# Preserve this comment\n"
            b"title: Keep\nnested:\n  helpx_example: Keep nested data\n...\nBody\n"
        )
        self.assertEqual(remove_helpx_metadata(original), (expected, 3))

    def test_unclosed_metadata_is_an_error(self):
        with self.assertRaisesRegex(ValueError, "closing delimiter"):
            remove_helpx_metadata(b"---\nhelpx_url: old\n")

    def test_all_fields_removed_and_idempotence(self):
        original = b"---\nhelpx_url: old\n---"
        updated, count = remove_helpx_metadata(original)
        self.assertEqual((updated, count), (b"---\n---", 1))
        self.assertEqual(remove_helpx_metadata(updated), (updated, 0))


class CommandTests(unittest.TestCase):
    def test_recursive_dry_run_and_removal(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            nested = root / "nested"
            nested.mkdir()
            first = root / "first.md"
            second = nested / "second.MD"
            untouched = root / "body.md"
            ignored = root / "other.txt"
            original = b"---\r\nhelpx_url: old\r\ntitle: Keep\r\n---\r\nBody"
            first.write_bytes(original)
            second.write_bytes(original)
            untouched.write_bytes(b"helpx_url: body text\n")
            ignored.write_bytes(original)
            before = {p: p.read_bytes() for p in (first, second, untouched, ignored)}

            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertEqual(main(["1", folder]), 0)
            self.assertIn("3 Markdown file(s) scanned", output.getvalue())
            self.assertIn("2 file(s) with 2 instance(s) found", output.getvalue())
            self.assertEqual({p: p.read_bytes() for p in before}, before)

            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(main(["2", folder]), 0)
            expected = original.replace(b"helpx_url: old\r\n", b"")
            self.assertEqual(first.read_bytes(), expected)
            self.assertEqual(second.read_bytes(), expected)
            self.assertEqual(untouched.read_bytes(), before[untouched])
            self.assertEqual(ignored.read_bytes(), before[ignored])

    def test_default_current_folder(self):
        from unittest.mock import patch

        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "example.md"
            path.write_bytes(b"---\nhelpx_url: old\n---\n")
            with patch("remove_helpx_metadta.Path.cwd", return_value=Path(folder)):
                with contextlib.redirect_stdout(io.StringIO()) as output:
                    self.assertEqual(main(["1"]), 0)
            self.assertIn("1 file(s) with 1 instance(s) found", output.getvalue())

    def test_invalid_arguments(self):
        for arguments in ([], ["3"], ["1", __file__]):
            with self.subTest(arguments=arguments):
                with contextlib.redirect_stderr(io.StringIO()):
                    with self.assertRaises(SystemExit) as error:
                        main(arguments)
                self.assertEqual(error.exception.code, 2)

    def test_reports_malformed_front_matter(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "broken.md"
            original = b"---\nhelpx_url: old\n"
            path.write_bytes(original)
            with contextlib.redirect_stdout(io.StringIO()):
                with contextlib.redirect_stderr(io.StringIO()) as errors:
                    self.assertEqual(main(["2", folder]), 1)
            self.assertIn("closing delimiter", errors.getvalue())
            self.assertEqual(path.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
