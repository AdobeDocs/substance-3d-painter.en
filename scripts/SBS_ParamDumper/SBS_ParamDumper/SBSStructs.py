import os

class SBSparam:
    def __init__(self, name, identifier, type, uitype, p_range=[], default=None, group = "", desc = ""):
        self.name = "" if name is None else name
        self.identifier = "" if identifier is None else identifier
        self.isinput = False
        self.default = default
        self.group = "" if group is None else group
        self.description = "" if desc is None else desc
        self.type = "unknown"
        if type == 1:
            self.type = "Color"
            self.isinput = True
        elif type == 2:
            self.type = "Grayscale"
            self.isinput = True
        elif type == 4:
            self.type = "Boolean"
        elif type == 16:
            self.type = "Integer"
        elif type == 32:
            self.type = "Integer2"
        elif type == 64:
            self.type = "Integer3"
        elif type == 128:
            self.type = "Integer4"
        elif type == 256:
            self.type = "Float"
        elif type == 512:
            self.type = "Float2"
        elif type == 1024:
            self.type = "Float3"
        elif type == 2048:
            self.type = "Float4"
        elif type == 16384:
            self.type = "String"

        self.uitype = uitype

        self.s_range = ""
        if len(p_range) > 0 and not self.isinput:
            if self.type == "Boolean":
                self.s_range = str(p_range[0]) + "/" + str(p_range[1])
            elif self.uitype == "dropdownlist":
                for v in p_range[:-1]:
                    seg = "" if v is None else str(v)
                    self.s_range += seg + ", "
                if len(p_range) > 0:
                    last = p_range[-1]
                    self.s_range += "" if last is None else str(last)
            elif self.uitype == "sizepow2":
                if len(p_range) >0:
                    self.s_range = "Resolution, " + str(p_range[0]) + " to " + str(p_range[1])
                else:
                    self.s_range = "Resolution, 1 to 12"
            elif self.uitype != "color" and self.uitype != "transformation" and uitype != "text":
                self.s_range = str(p_range[0]) + " - " + str(p_range[1])
            else:
                self.s_range = "" if not p_range or p_range[0] is None else str(p_range[0])
    def __str__(self):
        if not self.isinput:
            string = "\t"
            string += self.name + "\n"
            string += '\t\t\ttype: ' + self.type + '\n'
            string += '\t\t\trange: ' + self.s_range + '\n'
            string += '\t\t\tdefault: ' + str(self.default) + '\n'
            if self.group != "":
                string += '\t\t\tgroup: ' + self.group + '\n'
        else:
            string = '\t\t' + self.type + " " + self.name + "\n"
            if self.group != "":
                string += '\t\t\t\tgroup: ' + self.group + '\n'
        return string

class SBSgraph:
        def __init__(self, name, category, tags, thumbnail, description):
            self.name = "" if name is None else name
            self.category = "" if category is None else category
            self.tag = "" if tags is None else tags
            self.params = []
            self.inputs = []
            self.thumbnail = thumbnail
            self.description = "" if description is None else description

        def AddParam(self, param):
            try:
                if param.name != "":
                    if param.isinput:
                        self.inputs.append(param)
                    else:
                        self.params.append(param)
                    return True
                else:
                    return False
            except:
                return False

        def __str__(self):
            result = self.name + ' in ' + self.category + '/' + self.tag + ', with Parameters:\n'
            for param in self.params:
                result += "\t" + str(param)
            if len(self.inputs) > 0:
                result += "\t\tInputs: \n"
                for inp in self.inputs:
                    result += "\t" + str(inp)
            return result


class SBSdescription:

    def __init__(self, filename):
        self.filename = filename
        self.graphs = []

    def AddGraph(self, graph, p_skiptags=False):
        try:
            if graph.name != "" and graph.category != "":
                if p_skiptags:
                    self.graphs.append(graph)
                else:
                    if  graph.tag != "":
                        self.graphs.append(graph)
                    else:
                        print("warning, graph " + graph.name + " has category but no tags, skipping!")
                return True
            else:
                return False
        except:
            return False

    def __str__(self):
        result = "SBS Package, filename \'" + self.filename + "\' with graphs: \n"
        for g in self.graphs:
            result += "\t" + str(g)
        return result