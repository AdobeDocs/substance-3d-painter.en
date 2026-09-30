"""
Build full HTML documents for the Export tab live preview (HTML export or rendered Markdown).
"""

from __future__ import annotations

import html
import os
from collections.abc import Callable
from typing import Literal

from autofill_preset import AutofillPreset
from HTMLDumper import HTMLDumper
from MarkdownDumper import MarkdownDumper
from sbs_dump_config import SBSDumpConfig
from SBSreader import SBSReader

PreviewMode = Literal["html_rendered", "html_raw", "markdown_rendered", "markdown_raw"]


def _parse_sbs(path: str, config: SBSDumpConfig):
    reader = SBSReader(path, config=config)
    return reader.Parse()


MARKDOWN_PREVIEW_CSS = """
body { font-family: Segoe UI, system-ui, sans-serif; font-size: 14px; line-height: 1.5;
  margin: 16px; max-width: 52rem; color: #1a1a1a; }
h1 { font-size: 1.75rem; border-bottom: 1px solid #ddd; padding-bottom: 0.25em; }
h2, h3 { margin-top: 1.25em; }
code, pre { font-family: Consolas, "Courier New", monospace; font-size: 0.9em; }
pre { background: #f5f5f5; padding: 12px; overflow: auto; border-radius: 4px; }
code { background: #f0f0f0; padding: 2px 5px; border-radius: 3px; }
ul { padding-left: 1.5em; }
blockquote { border-left: 4px solid #ccc; margin-left: 0; padding-left: 1em; color: #444; }
"""


def _wrap_full_html(title: str, inner_body: str) -> str:
    t = html.escape(title, quote=True)
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{t}</title>
<style>{MARKDOWN_PREVIEW_CSS}</style></head><body>{inner_body}</body></html>"""


def preview_error_document(message: str) -> str:
    msg = html.escape(message, quote=False)
    return _wrap_full_html(
        "Preview error",
        f'<p style="color:#b00020;font-weight:600">Preview</p><p>{msg}</p>',
    )


def _ensure_html_document(fragment: str) -> str:
    low = fragment[:800].lower()
    if "<html" in low:
        return fragment
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"></head><body>{fragment}</body></html>"""


def _markdown_to_html_body(md_text: str) -> str:
    try:
        import markdown as md_lib

        try:
            body = md_lib.markdown(md_text, extensions=["extra", "nl2br"])
        except Exception:
            body = md_lib.markdown(md_text, extensions=["extra"])
        return body
    except ImportError:
        return f"<pre>{html.escape(md_text)}</pre><p><em>Tip: <code>pip install markdown</code> for formatted Markdown preview.</em></p>"


def _as_escaped_pre(text: str) -> str:
    return f"<pre>{html.escape(text)}</pre>"


def build_live_preview_html(
    sbs_path: str,
    config: SBSDumpConfig,
    autofill_path: str,
    mode: PreviewMode,
    log: Callable[[str], None] | None = None,
) -> tuple[str, str]:
    """
    Returns (full_html_document, status_message).
    status_message is empty on full success, or a short warning (e.g. preset fallback).
    If ``log`` is set, failures and warnings are also sent there (for the Export tab log).
    """

    def _emit(msg: str) -> None:
        if log:
            try:
                log(msg)
            except Exception:
                pass

    warnings: list[str] = []
    _emit(f"Preview start: mode={mode}, source={sbs_path}, preset={autofill_path}")
    try:
        autofill = AutofillPreset.from_file(autofill_path)
    except Exception as e:
        autofill = AutofillPreset.load_default()
        warnings.append(f"Preset issue (using defaults): {e}")
        _emit(warnings[-1])

    if not os.path.isfile(sbs_path):
        _emit("Not a file or file missing.")
        return preview_error_document("Not a file or file missing."), " ".join(warnings)

    try:
        desc = _parse_sbs(sbs_path, config)
    except Exception as e:
        _emit(f"Could not read XML: {e}")
        return preview_error_document(f"Could not read XML: {e}"), " ".join(warnings)

    if desc is None:
        _emit("Parser returned no package data.")
        return preview_error_document("Parser returned no package data."), " ".join(warnings)
    graph_count = len(getattr(desc, "graphs", []) or [])
    _emit(f"Parse result: {graph_count} graph(s) found.")
    if graph_count == 0:
        msg = (
            "No graphs matched current filters, so preview is empty. "
            "Check parsing options (especially 'Include graphs with an empty tag')."
        )
        _emit(msg)
        return preview_error_document(msg), " ".join(warnings)

    write_dummy = os.path.dirname(os.path.abspath(sbs_path)) or "."

    try:
        if mode in ("html_rendered", "html_raw"):
            hd = HTMLDumper(p_writefolder=write_dummy, p_config=config, p_autofill=autofill)
            fragment = hd.BuildHTML(desc)
            if not fragment:
                _emit("HTML output was empty.")
                return preview_error_document("HTML output was empty."), " ".join(warnings)
            doc = _ensure_html_document(fragment)
            if mode == "html_raw":
                doc = _wrap_full_html("HTML source", _as_escaped_pre(doc))
        else:
            md_d = MarkdownDumper(p_writefolder=write_dummy, p_config=config, p_autofill=autofill)
            md_text = md_d.BuildMarkdown(desc)
            if not md_text.strip():
                msg = "Markdown build produced empty output."
                _emit(msg)
                return preview_error_document(msg), " ".join(warnings)
            if mode == "markdown_raw":
                body = _as_escaped_pre(md_text)
            else:
                body = _markdown_to_html_body(md_text)
            doc = _wrap_full_html("Markdown preview", body)
    except Exception as e:
        _emit(f"Build failed: {e}")
        return preview_error_document(f"Build failed: {e}"), " ".join(warnings)

    if warnings:
        _emit(" | ".join(warnings))
    _emit(f"Preview success: html_length={len(doc)}")

    return doc, (" | ".join(warnings) if warnings else "")
