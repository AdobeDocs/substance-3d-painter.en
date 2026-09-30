import os
import platform
from glob import glob

import PNGDumper
from HTMLDumper import HTMLDumper
from sbs_dump_config import SBSDumpConfig
from SBSreader import SBSReader

osname = os.name
if osname.lower() == "posix":
    startpath = "/Applications/Substance Designer.app/Contents/Resources/packages"
elif osname.lower() == "nt":
    startpath = "C:\\Program Files\\Adobe\\Adobe Substance 3D Designer\\resources\\packages"

# filepath = easygui.fileopenbox(...)

filepath = os.path.join(startpath, "rt_caustics.sbs")

dump_config = SBSDumpConfig()


def ParseSingleFile(fp):
    if fp is not None:
        if os.path.exists(fp) and os.path.isfile(fp):
            reader = SBSReader(fp, config=dump_config)
            result = reader.Parse()
            return result
        else:
            print("invalid path: " + fp)
            return None


def DumpSingleFile(sbs):
    dumper = HTMLDumper(p_config=dump_config)
    html = dumper.BuildHTML(sbs)
    dumper.WriteToFile(html)


if os.path.isdir(filepath):
    result = [y for x in os.walk(filepath) for y in glob(os.path.join(x[0], '*.sbs'))]
    parsedfiles = []
    for f in result:
        parsed = ParseSingleFile(f)
        if parsed != None:
            parsedfiles.append(parsed)
    for p in parsedfiles:
        DumpSingleFile(p)
else:
    parsed = ParseSingleFile(filepath)
    DumpSingleFile(parsed)