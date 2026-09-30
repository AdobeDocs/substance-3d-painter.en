"""
Configurable Markdown output templates for MarkdownDumper.

Stored under the preset JSON key "markdown". All values are str.format templates
except nested_indent (plain string). Use {{ and }} for literal braces in templates.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

DEFAULT_MARKDOWN_FORMAT: dict[str, str] = {
    "graph_title": "# {title}\n",
    "location_line": "**In:** *{location}*\n",
    "graph_description": "{description}\n",
    "complexity_line": "{complexity}\n",
    "complexity_simple": "**Simple**",
    "complexity_intermediate": "**Intermediate**",
    "complexity_complex": "**Complex**",
    "complexity_unknown": "?",
    "inputs_heading": "### Inputs\n",
    "input_item": "- **{name}**: *{type} Input* {body}",
    "input_body": "{help}",
    "input_help_line": "  {help}",
    "input_help_empty": "",
    "parameters_heading": "### Parameters\n",
    "param_group_item": "- **{group}**",
    "param_row": "- **{name}**: *{range}* {body}",
    "nested_indent": "    ",
    "channels_bullet": "- {text}",
    "no_params": "*No parameters.{generator_note}*",
    "no_params_generator_note": " Remember you can always change base parameters such as the Random Seed.",
}

ALLOWED_MARKDOWN_KEYS = frozenset(DEFAULT_MARKDOWN_FORMAT.keys())


def _safe_format(tpl: str, **kwargs: Any) -> str:
    try:
        return tpl.format(**kwargs)
    except (KeyError, ValueError, IndexError):
        try:
            return tpl.format(**{k: str(v) for k, v in kwargs.items()})
        except Exception:
            return tpl


class MarkdownFormat:
    def __init__(self, data: dict[str, Any] | None = None):
        self._d = deepcopy(DEFAULT_MARKDOWN_FORMAT)
        if isinstance(data, dict):
            for k, v in data.items():
                if k in ALLOWED_MARKDOWN_KEYS and isinstance(v, str):
                    self._d[k] = v

    def get(self, key: str) -> str:
        return self._d.get(key, DEFAULT_MARKDOWN_FORMAT.get(key, ""))

    def complexity_label(self, key: str) -> str:
        k = f"complexity_{key}"
        if k in ALLOWED_MARKDOWN_KEYS and k in self._d:
            return self._d[k]
        return self.get("complexity_unknown")

    def format_graph_title(self, title: str) -> str:
        return _safe_format(self.get("graph_title"), title=title)

    def format_location_line(self, location: str) -> str:
        return _safe_format(self.get("location_line"), location=location)

    def format_graph_description(self, description: str) -> str:
        return _safe_format(self.get("graph_description"), description=description)

    def format_complexity_block(self, inner: str) -> str:
        if not inner:
            return ""
        return _safe_format(self.get("complexity_line"), complexity=inner)

    def format_input_item(self, name: str, type_name: str, body_text: str = "") -> str:
        tpl = self.get("input_item")
        row = _safe_format(
            tpl,
            name=name,
            type=type_name,
            **{"help": body_text, "body": body_text},
        )
        if body_text and ("{body}" not in tpl and "{help}" not in tpl):
            # Backward compatibility for old presets that used split input help lines.
            row = f"{row} {body_text}"
        return row

    def format_input_body(self, help_text: str) -> str:
        return _safe_format(self.get("input_body"), **{"help": help_text, "body": help_text})

    def format_input_help_line(self, help_text: str) -> str:
        return _safe_format(self.get("input_help_line"), **{"help": help_text})

    def format_param_group(self, group: str) -> str:
        return _safe_format(self.get("param_group_item"), group=group)

    def format_param_row(self, name: str, prange: str, body: str = "") -> str:
        tpl = self.get("param_row")
        row = _safe_format(tpl, name=name, **{"range": prange, "body": body})
        if body and "{body}" not in tpl:
            # Backward compatibility for old presets that used split body lines.
            row = f"{row} {body}"
        return row

    def format_channels_bullet(self, text: str) -> str:
        return _safe_format(self.get("channels_bullet"), text=text)

    def format_no_params(self, is_generators_category: bool) -> str:
        note = self.get("no_params_generator_note") if is_generators_category else ""
        return _safe_format(self.get("no_params"), generator_note=note)

    def to_dict(self) -> dict[str, str]:
        return {k: self._d[k] for k in sorted(ALLOWED_MARKDOWN_KEYS)}


def merge_markdown_defaults(data: dict[str, Any] | None) -> dict[str, str]:
    out = deepcopy(DEFAULT_MARKDOWN_FORMAT)
    if isinstance(data, dict):
        for k, v in data.items():
            if k in ALLOWED_MARKDOWN_KEYS and isinstance(v, str):
                out[k] = v
    return out
