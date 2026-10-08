# Remove legacy HelpX metadata

With Python 3.10 or later, run the following commands from the repository root:

```shell
python remove_helpx_metadta.py 1 <path>
python remove_helpx_metadta.py 2 <path>
```

Mode `1` is a dry run: it lists matching files and reports the number of files
scanned, files with matches, and matching metadata fields without changing files.
Mode `2` removes those fields and reports the removal counts. Omit `<path>` to
scan the current folder. Quote paths containing spaces.

The script recursively scans `.md` files (case-insensitive) and removes top-level
YAML front-matter fields whose names start with `helpx`, including their multiline
values. It preserves other metadata, comments, blank lines, Markdown content,
encoding, and line endings. It does not remove `helpx` references in the body.
Review the dry run before using mode `2`; removal edits files in place without
creating backups. File errors and unclosed front matter are reported and produce
a nonzero exit status. Files with unclosed front matter are left unchanged.