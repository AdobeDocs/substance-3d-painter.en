import os
import re

from autofill_preset import AutofillPreset
from sbs_dump_config import SBSDumpConfig


def _strip_html(text):
    if not text:
        return ""
    return re.sub(r"<[^>]+>", "", text).replace("&nbsp;", " ").strip()


def _md_inline(text):
    if not text:
        return ""
    s = _strip_html(str(text))
    return s.replace("\\", "\\\\").replace("*", "\\*")


class MarkdownDumper:
    def __init__(self, p_writefolder="", p_config: SBSDumpConfig | None = None, p_autofill=None):
        if p_writefolder == "":
            scriptfilename = os.path.realpath(__file__)
            scriptdir = os.path.dirname(scriptfilename)
            writedir = os.path.join(os.path.dirname(scriptdir), "Parameter Descriptions")
            if os.path.exists(writedir):
                self.writefolder = writedir
        else:
            if os.path.exists(p_writefolder):
                if os.path.isdir(p_writefolder):
                    self.writefolder = p_writefolder
                else:
                    self.writefolder = os.path.dirname(p_writefolder)
            else:
                os.makedirs(p_writefolder, exist_ok=True)
                self.writefolder = p_writefolder
        self.cfg = p_config if p_config is not None else SBSDumpConfig()
        self.channelsdone = False
        self.cat = ""
        self.tag = ""
        self.folderconflict = False

        if p_autofill is None:
            self.autofill = AutofillPreset.load_default()
        elif isinstance(p_autofill, AutofillPreset):
            self.autofill = p_autofill
        else:
            self.autofill = AutofillPreset.from_file(str(p_autofill))
        self.md = self.autofill.markdown_format

    def _complexity_key(self, graph) -> str | None:
        if not self.cfg.show_complexity_rating:
            return None
        np = len(graph.params)
        ni = len(graph.inputs)
        if graph.category == "Generators":
            if np < 5 and ni == 0:
                return "simple"
            if np < 10 and ni < 2:
                return "intermediate"
            if np >= 10 or ni <= 2:
                return "complex"
            return "unknown"
        if graph.category == "Filters":
            if graph.tag == "Blending":
                return "simple"
            if np < 5 and ni == 1:
                return "simple"
            if np < 10 and ni < 3:
                return "intermediate"
            if np >= 10 or ni >= 3:
                return "complex"
            return "unknown"
        if graph.category in ("Material Filters", "Mesh Adaptive"):
            ncp = sum(1 for p in graph.params if p.group != "Channels")
            if ncp < 5:
                return "simple"
            if ncp < 10:
                return "intermediate"
            if ncp >= 10:
                return "complex"
            return "unknown"
        if graph.category == "3D View":
            ncp = len(graph.params)
            if ncp < 5:
                return "simple"
            if ncp < 10:
                return "intermediate"
            if ncp >= 10:
                return "complex"
            return "unknown"
        return None

    def UISortParams(self, Params):
        result = []
        groupkeys = {}
        for p in Params:
            g = p.group
            if g == "":
                result.append(p)
            else:
                if g in groupkeys:
                    result[groupkeys[g]].append(p)
                else:
                    l = [p]
                    result.append(l)
                    groupkeys[g] = result.index(l)
        return result

    def AutoDescription(self, param):
        text = self.autofill.description_for_parameter(param.name, param.group)
        return text if text else ""

    def ParamPump(self, params):
        lines = []
        nest = self.md.get("nested_indent")
        for p in params:
            if isinstance(p, list):
                lines.append(self.md.format_param_group(_md_inline(p[0].group)))
                nested = self.ParamPump(p)
                for line in nested.split("\n"):
                    if line.strip():
                        lines.append(nest + line.lstrip())
            else:
                if p.group == "Channels":
                    if not self.channelsdone:
                        lines.append(
                            self.md.format_channels_bullet(self.autofill.channels_intro)
                        )
                        self.channelsdone = True
                else:
                    if not (
                        self.cfg.hide_workflow_normal_params
                        and p.identifier in ("workflow_type", "normal_format")
                    ):
                        body = _md_inline(p.description) if p.description else self.AutoDescription(p)
                        name = _md_inline(p.name)
                        rng = _md_inline(p.s_range)
                        # Keep each parameter as a single markdown entry (name + description).
                        lines.append(self.md.format_param_row(name, rng, body))
        return "\n".join(lines)

    def BuildMarkdown(self, description):
        self.filename = description.filename
        if description is None or len(description.graphs) == 0:
            return ""

        parts = []
        for graph in description.graphs:
            if self.cat == "":
                self.cat = graph.category
            elif self.cat != graph.category:
                print("Category conflict between " + self.cat + " and " + graph.category)
                self.folderconflict = True
            if self.cfg.check_tag_conflicts_for_output_layout:
                if self.tag == "":
                    self.tag = graph.tag
                elif self.tag != graph.tag:
                    print("Tag conflict between " + self.tag + " and " + graph.tag)
                    self.folderconflict = True
            elif self.cfg.nest_output_subfolder_by_tag and self.tag == "":
                self.tag = graph.tag

            title = _md_inline(graph.name)
            parts.append(self.md.format_graph_title(title))
            if self.cfg.show_graph_tag_in_header:
                loc = _md_inline(graph.category + "/" + graph.tag)
            else:
                loc = _md_inline(graph.category)
            parts.append(self.md.format_location_line(loc))
            ck = self._complexity_key(graph)
            if ck:
                inner = self.md.complexity_label(ck)
                block = self.md.format_complexity_block(inner)
                if block:
                    parts.append(block)
            if graph.description:
                parts.append(self.md.format_graph_description(_strip_html(graph.description)))
            if len(graph.inputs) > 1:
                parts.append(self.md.get("inputs_heading"))
                for i in graph.inputs:
                    if i.group != "Material":
                        iname = _md_inline(i.name)
                        itype = _md_inline(i.type)
                        help_txt = self.autofill.input_help_for_input(graph, i)
                        htxt = _md_inline(help_txt) if help_txt else ""
                        body = self.md.format_input_body(htxt) if htxt else ""
                        parts.append(self.md.format_input_item(iname, itype, body))
                parts.append("")

            if len(graph.params) > 0:
                self.channelsdone = False
                sortedparams = self.UISortParams(graph.params)
                parts.append(self.md.get("parameters_heading"))
                parts.append(self.ParamPump(sortedparams))
                parts.append("")
            else:
                is_gen = graph.category == "Generators:"
                parts.append(self.md.format_no_params(is_gen) + "\n")

        return "\n".join(parts).rstrip() + "\n"

    def ensure_dir(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def WriteToFile(self, data):
        if self.filename is None or not data or self.tag in ("Deprecated", "Deprecqted"):
            print("did not write markdown for " + str(self.filename))
            if self.tag in ("Deprecated", "Deprecqted"):
                print("reason:deprecated")
            return None
        if not self.folderconflict:
            fullpath = os.path.join(self.writefolder, self.cat)
            self.ensure_dir(fullpath)
            if self.cfg.nest_output_subfolder_by_tag:
                fullpath = os.path.join(fullpath, self.tag)
                self.ensure_dir(fullpath)
            fullpath = os.path.join(fullpath, self.filename + ".md")
        else:
            fullpath = os.path.join(self.writefolder, self.filename + ".md")
        with open(fullpath, "w", encoding="utf-8") as h:
            h.write(data)
        print("wrote markdown file to " + fullpath)
        return fullpath
