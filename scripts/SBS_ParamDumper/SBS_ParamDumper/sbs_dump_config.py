"""Neutral export/parsing options (not tied to a specific app name)."""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from typing import Any, Literal


CategorySource = Literal["xml", "folder"]


@dataclass(frozen=True)
class SBSDumpConfig:
    # --- Parsing ---
    category_source: CategorySource = "folder"
    """xml: category from graph attributes; folder: category from parent folder name."""
    normalize_xml_category_names: bool = True
    """When category_source is xml: map e.g. Filter → Filters, Generator → Generators."""
    remap_graph_tags: bool = True
    """Normalize tag strings (e.g. Blur → Blurs) for library-style grouping."""
    allow_graphs_without_tag: bool = False
    """If False, graphs with an empty tag are skipped (with a warning)."""

    # --- HTML / Markdown output ---
    show_complexity_rating: bool = True
    hide_workflow_normal_params: bool = False
    """Omit workflow_type and normal_format from parameter lists when True."""
    show_graph_tag_in_header: bool = True
    """Location line shows category/tag vs category only."""
    check_tag_conflicts_for_output_layout: bool = True
    """Multiple graphs with different tags → flat output path when conflict."""
    nest_output_subfolder_by_tag: bool = True
    """Place files under output/<category>/<tag>/ when there is no conflict."""

    @classmethod
    def folder_library_style(cls) -> SBSDumpConfig:
        """Preset matching the old “folder category + flat output” pipeline."""
        return cls(
            category_source="folder",
            normalize_xml_category_names=False,
            remap_graph_tags=False,
            allow_graphs_without_tag=True,
            show_complexity_rating=False,
            hide_workflow_normal_params=True,
            show_graph_tag_in_header=False,
            check_tag_conflicts_for_output_layout=False,
            nest_output_subfolder_by_tag=False,
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any] | None) -> SBSDumpConfig:
        if not data:
            return cls()
        cur = cls()
        kwargs: dict[str, Any] = {}
        for f in cur.__dataclass_fields__:
            if f in data:
                val = data[f]
                if f == "category_source" and val not in ("xml", "folder"):
                    continue
                if f != "category_source" and not isinstance(val, bool):
                    continue
                kwargs[f] = val
        return replace(cur, **kwargs) if kwargs else cur
