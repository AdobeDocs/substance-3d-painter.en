import os
from glob import glob

import PNGDumper
from HTMLDumper import HTMLDumper
from sbs_dump_config import SBSDumpConfig
from SBSreader import SBSReader

osname = os.name
if osname.lower() == "posix":
    startpath = "/Applications/Substance Designer.app/Contents/Resources/packages"
elif osname.lower() == "nt":
    startpath = "C:\\Program Files\\Allegorithmic\\Substance Designer\\resources\\packages\\"

writefolder = "C:\\Users\\Laurens\\Desktop\\Filter HTML\\"

filepath = "F:\\OneDrive - Adobe\\Documentation\\Sampler\\SBS"

dump_config = SBSDumpConfig.folder_library_style()


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
    dumper = HTMLDumper(p_writefolder=writefolder, p_config=dump_config)
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