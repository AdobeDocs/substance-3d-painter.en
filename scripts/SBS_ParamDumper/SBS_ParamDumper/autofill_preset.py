"""
Load and resolve autofill presets (parameter names, blending templates, input slot rules).

Preset files are JSON. Parameter values may use "@OtherKey" to reuse another entry's text.
Input matching uses ordered rules: first match wins.
"""

from __future__ import annotations

import json
import os
import re
from typing import Any

from markdown_format import MarkdownFormat, merge_markdown_defaults

DEFAULT_CHANNELS_INTRO = (
    "Toggle material channels on and off in this group, when using Specular/Glossiness maps "
    "instead of Metallic/Roughness for example."
)

DEFAULT_BLENDING_TEMPLATE = "Blending strength of the {key}."

# Legacy flat dict (pre–input_rules) — used only for migration
_LEGACY_INPUT_KEYS: dict[str, str] = {
    "mask_intro": "Mask slot used for masking the node's effects.",
    "mask_toggle_suffix": ' Can be toggled with the "{mask_param}" parameter.',
    "ambient_curvature": "Baked map used for internal effects and masking",
    "normal_ws": "Baked WorldSpace Normal map used for internal effects and masking.",
    "pattern_intro": "Custom pattern image",
    "pattern_suffix": ', used when the "{pattern_param}" parameter is set to "Image Input"',
}


def default_input_rules() -> list[dict[str, Any]]:
    """Default ordered rules equivalent to the original hard-coded input logic."""
    L = _LEGACY_INPUT_KEYS
    return [
        {
            "id": "mask",
            "match_type": "contains",
            "match_value": "Mask",
            "text": L["mask_intro"],
            "append_boolean_toggle": True,
            "toggle_lookup_param_names": ["Mask", "Use Mask", "Alpha Blending"],
            "toggle_template": L["mask_toggle_suffix"],
        },
        {
            "id": "ao_curvature",
            "match_type": "equals_any",
            "match_values": ["Ambient Occlusion", "Curvature"],
            "text": L["ambient_curvature"],
        },
        {
            "id": "normal_ws",
            "match_type": "equals",
            "match_value": "Normal WS",
            "text": L["normal_ws"],
        },
        {
            "id": "pattern_image_input",
            "match_type": "all_contain",
            "match_values": ["Pattern", "Input"],
            "text": L["pattern_intro"],
            "append_pattern_dropdown": True,
            "pattern_lookup_param_names": ["Pattern Type", "Pattern"],
            "pattern_suffix_template": L["pattern_suffix"],
            "append_period": True,
        },
    ]


def legacy_inputs_dict_to_rules(inputs: dict[str, str]) -> list[dict[str, Any]]:
    """Build input_rules from an old preset `inputs` object."""
    merged = dict(_LEGACY_INPUT_KEYS)
    for k, v in inputs.items():
        s = str(v).strip()
        if s:
            merged[str(k)] = s
    L = merged
    return [
        {
            "id": "mask",
            "match_type": "contains",
            "match_value": "Mask",
            "text": L["mask_intro"],
            "append_boolean_toggle": True,
            "toggle_lookup_param_names": ["Mask", "Use Mask", "Alpha Blending"],
            "toggle_template": L["mask_toggle_suffix"],
        },
        {
            "id": "ao_curvature",
            "match_type": "equals_any",
            "match_values": ["Ambient Occlusion", "Curvature"],
            "text": L["ambient_curvature"],
        },
        {
            "id": "normal_ws",
            "match_type": "equals",
            "match_value": "Normal WS",
            "text": L["normal_ws"],
        },
        {
            "id": "pattern_image_input",
            "match_type": "all_contain",
            "match_values": ["Pattern", "Input"],
            "text": L["pattern_intro"],
            "append_pattern_dropdown": True,
            "pattern_lookup_param_names": ["Pattern Type", "Pattern"],
            "pattern_suffix_template": L["pattern_suffix"],
            "append_period": True,
        },
    ]


def normalize_input_rule(rule: dict[str, Any]) -> dict[str, Any]:
    out = dict(rule)
    out["id"] = str(out.get("id", "rule")).strip() or "rule"
    out["match_type"] = str(out.get("match_type", "contains")).strip().lower()
    out["match_value"] = str(out.get("match_value", ""))
    mv = out.get("match_values")
    if isinstance(mv, list):
        out["match_values"] = [str(x).strip() for x in mv if str(x).strip()]
    else:
        out["match_values"] = []
    out["text"] = str(out.get("text", ""))
    out["append_boolean_toggle"] = bool(out.get("append_boolean_toggle"))
    tnames = out.get("toggle_lookup_param_names")
    if isinstance(tnames, list):
        out["toggle_lookup_param_names"] = [str(x).strip() for x in tnames if str(x).strip()]
    else:
        out["toggle_lookup_param_names"] = ["Mask", "Use Mask", "Alpha Blending"]
    out["toggle_template"] = str(
        out.get("toggle_template") or _LEGACY_INPUT_KEYS["mask_toggle_suffix"]
    )
    out["append_pattern_dropdown"] = bool(out.get("append_pattern_dropdown"))
    pnames = out.get("pattern_lookup_param_names")
    if isinstance(pnames, list):
        out["pattern_lookup_param_names"] = [str(x).strip() for x in pnames if str(x).strip()]
    else:
        out["pattern_lookup_param_names"] = ["Pattern Type", "Pattern"]
    out["pattern_suffix_template"] = str(
        out.get("pattern_suffix_template") or _LEGACY_INPUT_KEYS["pattern_suffix"]
    )
    out["append_period"] = bool(out.get("append_period"))
    return out


def rule_matches_input(rule: dict[str, Any], input_name: str) -> bool:
    r = normalize_input_rule(rule)
    mt = r["match_type"]
    name = input_name
    if mt == "contains":
        return bool(r["match_value"]) and r["match_value"] in name
    if mt == "equals":
        return name == r["match_value"]
    if mt == "equals_any":
        return name in r["match_values"]
    if mt == "all_contain":
        return bool(r["match_values"]) and all(sub in name for sub in r["match_values"])
    if mt == "regex":
        try:
            return bool(re.search(r["match_value"], name))
        except re.error:
            return False
    return False


def build_input_help_text(graph: Any, inp: Any, rule: dict[str, Any]) -> str:
    """Build help string for one input using a matched rule and graph context."""
    r = normalize_input_rule(rule)
    parts: list[str] = [r["text"]]

    if r["append_boolean_toggle"]:
        names = r["toggle_lookup_param_names"]
        tpl = r["toggle_template"]
        for p in graph.params:
            if p.name in names and p.type == "Boolean":
                try:
                    parts.append(tpl.format(mask_param=p.name))
                except (KeyError, ValueError):
                    parts.append(_LEGACY_INPUT_KEYS["mask_toggle_suffix"].format(mask_param=p.name))
                break

    if r["append_pattern_dropdown"]:
        pnames = r["pattern_lookup_param_names"]
        tpl = r["pattern_suffix_template"]
        for p in graph.params:
            if p.name in pnames:
                try:
                    parts.append(tpl.format(pattern_param=p.name))
                except (KeyError, ValueError):
                    parts.append(
                        _LEGACY_INPUT_KEYS["pattern_suffix"].format(pattern_param=p.name)
                    )
                break
        if r["append_period"]:
            parts.append(".")

    return "".join(parts)


def script_dir() -> str:
    return os.path.dirname(os.path.realpath(__file__))


def default_presets_dir() -> str:
    return os.path.join(script_dir(), "presets")


def default_preset_path() -> str:
    return os.path.join(default_presets_dir(), "designer_default.json")


def list_preset_paths(directory: str) -> list[str]:
    if not os.path.isdir(directory):
        return []
    out = []
    for name in sorted(os.listdir(directory)):
        if name.lower().endswith(".json"):
            out.append(os.path.join(directory, name))
    return out


def _resolve_parameter_refs(raw: dict[str, str], max_passes: int = 64) -> dict[str, str]:
    """Expand @Key references to final strings."""
    out = dict(raw)
    for _ in range(max_passes):
        changed = False
        for k, v in list(out.items()):
            if not isinstance(v, str):
                continue
            if v.startswith("@") and len(v) > 1:
                ref = v[1:]
                if ref in out and not (isinstance(out[ref], str) and out[ref].startswith("@")):
                    out[k] = out[ref]
                    changed = True
        if not changed:
            break
    return out


class AutofillPreset:
    def __init__(self, data: dict[str, Any], source_path: str | None = None):
        self.source_path = source_path
        self.version = int(data.get("version", 1))
        self.display_name = str(data.get("display_name", "Preset"))
        raw_params = data.get("parameters")
        if not isinstance(raw_params, dict):
            raw_params = {}
        self._parameters_raw = {str(k): str(v) for k, v in raw_params.items()}
        self.parameters = _resolve_parameter_refs(dict(self._parameters_raw))
        bt = str(data.get("blending_intensity_template", DEFAULT_BLENDING_TEMPLATE)).strip()
        self.blending_intensity_template = bt if bt else DEFAULT_BLENDING_TEMPLATE
        ch = str(data.get("channels_intro", DEFAULT_CHANNELS_INTRO)).strip()
        self.channels_intro = ch if ch else DEFAULT_CHANNELS_INTRO

        rules = data.get("input_rules")
        if isinstance(rules, list):
            self.input_rules = [normalize_input_rule(x) for x in rules if isinstance(x, dict)]
        else:
            legacy = data.get("inputs")
            if isinstance(legacy, dict) and legacy:
                self.input_rules = [
                    normalize_input_rule(x) for x in legacy_inputs_dict_to_rules(legacy)
                ]
            else:
                self.input_rules = [normalize_input_rule(x) for x in default_input_rules()]

        md = data.get("markdown")
        self.markdown_format = MarkdownFormat(md if isinstance(md, dict) else None)

    def raw_parameters(self) -> dict[str, str]:
        """Unresolved parameter map as stored in JSON (may contain @Key references)."""
        return dict(self._parameters_raw)

    def description_for_parameter(self, param_name: str, param_group: str) -> str | None:
        if param_group == "Blending":
            suf = " Intensity"
            if suf in param_name:
                key = param_name.replace(suf, "")
                try:
                    return self.blending_intensity_template.format(key=key)
                except (KeyError, ValueError):
                    return DEFAULT_BLENDING_TEMPLATE.format(key=key)
            return None
        if param_name in self.parameters:
            return self.parameters[param_name]
        return None

    def input_help_for_input(self, graph: Any, inp: Any) -> str | None:
        """First matching rule wins. Returns None if no rule matches."""
        name = inp.name or ""
        for rule in self.input_rules:
            if rule_matches_input(rule, name):
                return build_input_help_text(graph, inp, rule)
        return None

    @staticmethod
    def from_file(path: str) -> AutofillPreset:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("Preset root must be a JSON object")
        return AutofillPreset(data, source_path=path)

    @staticmethod
    def load_default() -> AutofillPreset:
        p = default_preset_path()
        if os.path.isfile(p):
            return AutofillPreset.from_file(p)
        return AutofillPreset(
            {
                "version": 1,
                "display_name": "Built-in fallback",
                "parameters": {},
                "blending_intensity_template": DEFAULT_BLENDING_TEMPLATE,
                "channels_intro": DEFAULT_CHANNELS_INTRO,
                "input_rules": default_input_rules(),
                "markdown": merge_markdown_defaults(None),
            }
        )

    def to_serializable_dict(self) -> dict[str, Any]:
        return {
            "version": self.version,
            "display_name": self.display_name,
            "parameters": dict(self._parameters_raw),
            "blending_intensity_template": self.blending_intensity_template,
            "channels_intro": self.channels_intro,
            "input_rules": list(self.input_rules),
            "markdown": self.markdown_format.to_dict(),
        }


def empty_input_rule() -> dict[str, Any]:
    """New rule for the preset editor (sensible defaults)."""
    return {
        "id": "new_rule",
        "match_type": "contains",
        "match_value": "",
        "match_values": [],
        "text": "",
        "append_boolean_toggle": False,
        "toggle_lookup_param_names": ["Mask", "Use Mask", "Alpha Blending"],
        "toggle_template": _LEGACY_INPUT_KEYS["mask_toggle_suffix"],
        "append_pattern_dropdown": False,
        "pattern_lookup_param_names": ["Pattern Type", "Pattern"],
        "pattern_suffix_template": _LEGACY_INPUT_KEYS["pattern_suffix"],
        "append_period": False,
    }


def ensure_presets_dir() -> None:
    os.makedirs(default_presets_dir(), exist_ok=True)
