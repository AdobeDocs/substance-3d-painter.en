import base64, os

class PNGDumper:
    def __init__(self, p_writefolder=""):
        if p_writefolder == "":
            scriptfilename = os.path.realpath(__file__)
            scriptdir = os.path.dirname(scriptfilename)
            writedir = os.path.join(os.path.dirname(scriptdir),"Parameter Descriptions")
            if os.path.exists(writedir):
                self.writefolder = writedir
                #print "Writing folder determined to be \"" + writedir + "\"."
        else:
            self.writefolder = p_writefolder

        self.cat = ""
        self.tag = ""
        self.folderconflict = False

    def writeBase64PNG(self, filename, pngtext):
        g = open(os.path.join(self.writefolder,filename+".png"), "w")
        g.write(pngtext.decode('base64'))
        g.close()