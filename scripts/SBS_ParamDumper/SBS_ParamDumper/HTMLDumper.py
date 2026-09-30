import os

from autofill_preset import AutofillPreset
from sbs_dump_config import SBSDumpConfig
from SBSStructs import SBSdescription


class HTMLDumper:
    def __init__(self, p_writefolder="", p_config: SBSDumpConfig | None = None, p_autofill=None):
        if p_writefolder == "":
            scriptfilename = os.path.realpath(__file__)
            scriptdir = os.path.dirname(scriptfilename)
            writedir = os.path.join(os.path.dirname(scriptdir),"Parameter Descriptions")
            if os.path.exists(writedir):
                self.writefolder = writedir
                #print "Writing folder determined to be \"" + writedir + "\"."
        else:
            if os.path.exists(p_writefolder):
                if os.path.isdir(p_writefolder):
                    self.writefolder = p_writefolder
                else:
                    self.writefolder = os.path.dirname(p_writefolder)
            else:
                print("Htmldumper: path " + p_writefolder + " does not exist, creating.")
                os.mkdir(p_writefolder)
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

    def DetermineComplexity(self,graph):

        simple = "<span style=\"color: rgb(0, 128, 0);\"><strong>Simple</strong></span>\n"
        intermediate = "<span style=\"color: rgb(255, 102, 0);\"><strong>Intermediate</strong></span>\n"
        complex = "<span style=\"color: rgb(128, 0, 0);\"><strong>Complex</strong></span>\n"
        unknown = "?"
        if not self.cfg.show_complexity_rating:
            return ""

        np = len(graph.params)
        ni = len(graph.inputs)

        if graph.category == "Generators":
            if np < 5 and ni ==0:
                return simple
            elif np < 10 and ni <2:
                return intermediate
            elif np >= 10 or ni <= 2:
                return complex
            else:
                return unknown
        elif graph.category == "Filters":
            if graph.tag == "Blending":
                return simple
            elif np < 5 and ni ==1:
                return simple
            elif np < 10 and ni <3:
                return intermediate
            elif np >= 10 or ni >= 3:
                return complex
            else:
                return unknown
        elif graph.category == "Material Filters" or graph.category == "Mesh Adaptive":
            ncp = 0
            for p in graph.params:
                if p.group != "Channels":
                    ncp += 1
            if ncp < 5:
                return simple
            elif ncp < 10:
                return intermediate
            elif ncp >= 10:
                return complex
            else:
                return unknown
        elif graph.category == "3D View":
            ncp = 0
            for p in graph.params:
                ncp += 1
            if ncp < 5:
                return simple
            elif ncp < 10:
                return intermediate
            elif ncp >= 10:
                return complex
            else:
                return unknown
        return ""

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
                    l =[p]
                    result.append(l)
                    groupkeys[g] = result.index(l)
        return result

    def AutoDescription(self, param):
        text = self.autofill.description_for_parameter(param.name, param.group)
        if text:
            return text
        return "<br>"

    def ParamPump(self, params):
        html = ""
        html += "<ul>\n"
        for p in params:
            if isinstance(p, list):
                html += "<li>\n"
                html += "<strong>" + p[0].group + "</strong>\n<br>\n"
                html += self.ParamPump(p)
                html += "</li>\n"
            else:
                if p.group == "Channels":
                    if self.channelsdone == False:
                        html += "<li>\n"
                        html += self.autofill.channels_intro + "\n"
                        html += "</li>\n"
                        self.channelsdone = True
                else:
                    if not (
                        self.cfg.hide_workflow_normal_params
                        and p.identifier in ("workflow_type", "normal_format")
                    ):
                        html += "<li>\n"
                        html += "<strong>" + p.name + "</strong>: <em>" + p.s_range + "</em>"
                        html += "<br>"
                        if p.description == "":
                            html += self.AutoDescription(p)
                        else:
                            html += p.description
                        html += "</li>\n"
        html += "</ul>\n"
        return html

    def BuildHTML(self, description):
        self.filename = description.filename
        if description!= None:

            html = ""
            if len(description.graphs) == 0:
                return html

            html += "<html>\n<body>\n"

            for graph in description.graphs:
                if self.cat == "":
                    self.cat = graph.category
                else:
                    if self.cat != graph.category:
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

                html += "<div>\n"
                html += "<h1 style=\"text-align: center;\" data-mce-style=\"text-align: center;\">" + graph.name + "</h1>\n"
                html += "<p style=\"text-align: center;\" data-mce-style=\"text-align: center;\">\n"
                if self.cfg.show_graph_tag_in_header:
                    html += "<strong>In:</strong>\n<em>" + graph.category + "/" + graph.tag + "</em>"
                else:
                    html += "<strong>In:</strong>\n<em>" + graph.category + "</em>"
                html += "</p><p style=\"text-align: center;\" data-mce-style=\"text-align: center;\">\n"
                html += self.DetermineComplexity(graph)
                html += "</p>"

                if graph.description != "":
                    html += "<br>\n"
                    html += graph.description +"\n"
                    html += "<br>\n"

                if len(graph.inputs) > 1:
                    html += "<h3>" + "Inputs" + "</h3>\n"
                    html += "<ul>\n"
                    for i in graph.inputs:
                        if i.group != "Material":
                            html += "<li>\n"
                            html += "<strong>" + i.name + "</strong>: <em>" + i.type + " Input</em>\n"
                            html += "<br>\n"
                            help_txt = self.autofill.input_help_for_input(graph, i)
                            if help_txt is not None:
                                html += help_txt + "\n"
                            else:
                                html += "<br/>\n"
                            html += "</li>\n"
                    html += "</ul>\n"

                if len(graph.params) > 0:
                    sortedparams = self.UISortParams(graph.params)
                    html += "<h3>" + "Parameters" + "</h3>\n"
                    html += self.ParamPump(sortedparams)
                else:
                    html += "<em>No Parameters."
                    if graph.category == "Generators:":
                        html += "Remember you can always change base parameters such as the Random Seed."
                    html += "</em>\n"

                html += "</div>\n"

            html += "</body>\n</html>\n"

            return html
        else:
            return None

    def ensure_dir(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def WriteToFile(self, data):
        if self.filename != None and data != None and data != "" and self.tag != "Deprecated" and self.tag != "Deprecqted":
            if not self.folderconflict:
                fullpath = os.path.join(self.writefolder, self.cat)
                self.ensure_dir(fullpath)
                if self.cfg.nest_output_subfolder_by_tag:
                    fullpath = os.path.join(fullpath, self.tag)
                    self.ensure_dir(fullpath)
                fullpath = os.path.join(fullpath, self.filename + ".html")
            else:
                fullpath = os.path.join(self.writefolder, self.filename + ".html")
            h = open(fullpath,'w')
            h.write(data)
            print("wrote htmlfile to " + fullpath)
            h.close()
            return fullpath
        else:
            print("did not write data for " + str(self.filename))
            if self.tag == "Deprecated" or self.tag == "Deprecqted":
                print("reason:deprecated")
            elif data == None or data == "":
                print("reason:data == none")
            return None
