import os
import xml.etree.ElementTree as ET

from sbs_dump_config import SBSDumpConfig
from SBSStructs import SBSdescription, SBSgraph, SBSparam


def _xml_v(elem, default=""):
    """Return Substance XML ``v`` attribute as str; missing element or attribute -> default."""
    if elem is None:
        return default
    val = elem.get("v")
    return default if val is None else val


class SBSReader:

    def __init__(self, parsepath, config: SBSDumpConfig | None = None):
        self.ParsePath = parsepath
        self.config = config if config is not None else SBSDumpConfig()

    def CheckIfSBS(self, l_path):
        if os.path.isfile(l_path):
            if os.path.splitext(l_path)[1].lower() == ".sbs":
                return True
        else:
            return False

    def Typecast(self, type, value):
        if type == 16:
            return int(value)
        elif type == 32 or type == 64 or type == 128:
            l = value.split(";")
            if len(l) == 1:
                return int(l[0])
            else:
                return str(l)
        if type == 256:
            return float(value)
        elif type == 512 or type == 1024 or type == 2048:
            l = value.split(";")
            if len(l) == 1:
                return float(l[0])
            else:
                return str(l)

    def _category_from_folder(self, sbspath: str) -> str:
        try:
            return os.path.basename(os.path.dirname(sbspath))
        except (IndexError, TypeError):
            return ""

    def _category_from_xml(self, atts) -> str:
        cat = ""
        c_el = atts.find("category")
        if c_el is not None:
            cat = _xml_v(c_el) or ""
            if self.config.normalize_xml_category_names:
                if cat == "Filter":
                    cat = "Filters"
                elif cat == "Material Filter":
                    cat = "Material Filters"
                elif cat == "Generator":
                    cat = "Generators"
                elif cat.casefold() == "filters":
                    cat = "Filters"
                elif cat.casefold() == "generators":
                    cat = "Generators"
                elif cat.casefold() == "material filter":
                    cat = "Material Filters"
        return cat

    def _tags_from_xml(self, tags_raw: str) -> str:
        tags = tags_raw
        if not self.config.remap_graph_tags:
            return tags
        if tags == "Blur":
            return "Blurs"
        if "Effect" in tags:
            return "Effects"
        if "Transformation" in tags:
            return "Transforms"
        if "blending" in tags:
            return "Blending"
        if tags == "Noise":
            return "Noises"
        if "Pattern" in tags:
            return "Patterns"
        if "Adjustment" in tags:
            return "Adjustments"
        if "Channel" in tags:
            return "Channels"
        return tags

    def getParamsFromGraph(self, graph):
        SBSparams = []
        if graph is not None:
            params = graph.find("paraminputs")
            if params is not None:
                for param in params.findall("paraminput"):
                    ident_el = param.find("identifier")
                    identifier = _xml_v(ident_el)
                    atts = param.find("attributes")
                    if atts is not None:
                        label_el = atts.find("label")
                        paramname = _xml_v(label_el) if label_el is not None else identifier
                        if not paramname:
                            paramname = identifier
                        desc_el = atts.find("description")
                        paramdesc = _xml_v(desc_el) if desc_el is not None else ""
                    else:
                        paramname = identifier
                        paramdesc = ""
                    paramtype = int(_xml_v(param.find("type"), "0"))
                    paramrange = []
                    paramdefault = ""
                    dw = param.find("defaultWidget")
                    name_el = dw.find("name") if dw is not None else None
                    uitype = _xml_v(name_el) if name_el is not None else ""
                    options = dw.find("options") if dw is not None else None

                    group_el = param.find("group")
                    paramgroup = _xml_v(group_el) if group_el is not None else ""

                    if options is None:
                        options = []

                    if uitype == "buttons":
                        paramrange = ["False", "True"]
                        for option in options:
                            on = option.find("name")
                            ov = option.find("value")
                            optname = _xml_v(on)
                            optvalue = _xml_v(ov)
                            if optname == "label0":
                                paramrange[0] = optvalue
                            elif optname == "label1":
                                paramrange[1] = optvalue
                            elif optname == "default":
                                paramdefault = int(optvalue or "0")
                    elif uitype == "slider" or uitype == "angle":
                        paramrange = ["", ""]
                        for option in options:
                            on = option.find("name")
                            ov = option.find("value")
                            optname = _xml_v(on)
                            optvalue = _xml_v(ov)
                            if optname == "min":
                                paramrange[0] = self.Typecast(paramtype, optvalue)
                            elif optname == "max":
                                paramrange[1] = self.Typecast(paramtype, optvalue)
                            elif optname == "default":
                                paramdefault = self.Typecast(paramtype, optvalue)
                    elif uitype == "dropdownlist":
                        for option in options:
                            ov = option.find("value")
                            raw = _xml_v(ov)
                            if not raw:
                                continue
                            bits = raw.split(";")
                            paramrange = bits[2::2] if len(bits) > 2 else []
                            try:
                                paramdefault = int(bits[0])
                            except (ValueError, IndexError):
                                paramdefault = 0
                    elif uitype == "text":
                        paramrange = ["(Text String)"]
                        for option in options:
                            on = option.find("name")
                            ov = option.find("value")
                            optname = _xml_v(on)
                            optvalue = _xml_v(ov)
                            if optname == "default":
                                paramdefault = optvalue
                    elif uitype == "color":
                        if paramtype == 256:
                            paramrange = ["(Grayscale value)"]
                        elif paramtype == 2048 or paramtype == 1024:
                            paramrange = ["(Color value)"]
                        for option in options:
                            on = option.find("name")
                            ov = option.find("value")
                            optname = _xml_v(on)
                            optvalue = _xml_v(ov)
                            if optname == "default":
                                paramdefault = optvalue
                    elif uitype == "transformation":
                        paramrange = ["(Transformation Matrix)"]
                        for option in options:
                            on = option.find("name")
                            ov = option.find("value")
                            optname = _xml_v(on)
                            optvalue = _xml_v(ov)
                            if optname == "default":
                                paramdefault = optvalue
                    elif uitype == "sizepow2":
                        paramrange = [1, 12]
                        for option in options:
                            on = option.find("name")
                            ov = option.find("value")
                            optname = _xml_v(on)
                            optvalue = _xml_v(ov)
                            if optname == "default":
                                paramdefault = optvalue

                    SBSparams.append(
                        SBSparam(
                            paramname,
                            identifier,
                            paramtype,
                            uitype,
                            paramrange,
                            paramdefault,
                            paramgroup,
                            paramdesc,
                        )
                    )

        return SBSparams

    def ParseSingleSBS(self, sbspath):
        if not os.path.exists(sbspath):
            return None
        tree = ET.parse(sbspath)
        root = tree.getroot()
        SBSdesc = None
        identifier = root.find("identifier")
        if identifier is not None:
            sbsname = _xml_v(identifier)
            if (sbsname or "").lower() == "unsaved package":
                sbsname = os.path.splitext(os.path.basename(sbspath))[0]
            if sbsname:
                SBSdesc = SBSdescription(sbsname)
        if SBSdesc is None:
            return None
        content = root.find("content")
        if content is None:
            return SBSdesc
        graphs = content.findall("graph")
        if not graphs:
            return SBSdesc
        for graph in graphs:
            atts = graph.find("attributes")
            if atts is None:
                continue
            hide_el = atts.find("hideInLibrary")
            hide = int(hide_el.get("v")) if hide_el is not None else 0
            if hide == 1:
                continue
            name_el = atts.find("label")
            if name_el is not None:
                name = _xml_v(name_el)
            else:
                rid = root.find("identifier")
                name = _xml_v(rid) if rid is not None else ""
            if not name:
                name = os.path.splitext(os.path.basename(sbspath))[0]
            tags_el = atts.find("tags")
            tags_raw = _xml_v(tags_el) if tags_el is not None else ""
            tags = self._tags_from_xml(tags_raw)
            desc_el = atts.find("description")
            desc = _xml_v(desc_el) if desc_el is not None else ""
            icon = atts.find("icon")
            if icon is not None:
                strdata_el = icon.find("strdata")
                strdata = _xml_v(strdata_el) if strdata_el is not None else ""
            else:
                strdata = ""

            if self.config.category_source == "folder":
                cat = self._category_from_folder(sbspath)
            else:
                cat = self._category_from_xml(atts)

            currentgraph = SBSgraph(name, cat, tags, strdata, desc)
            for param in self.getParamsFromGraph(graph):
                currentgraph.AddParam(param)
            SBSdesc.AddGraph(
                currentgraph,
                p_skiptags=self.config.allow_graphs_without_tag,
            )

        return SBSdesc

    def Parse(self):
        if self.CheckIfSBS(self.ParsePath):
            return self.ParseSingleSBS(self.ParsePath)
        sbslist = []
        for f in os.listdir(self.ParsePath):
            full = os.path.join(self.ParsePath, f)
            if self.CheckIfSBS(full):
                parsed = self.ParseSingleSBS(full)
                if parsed is not None:
                    sbslist.append(parsed)
        return sbslist
