#Data Structures
#TO-DO
import os
import glob

class datastruct:
    dataPath = 'Data/'

    def __init__(self):
        try:
            os.makedirs(self.dataPath)
        except OSError:
            if not os.path.isdir(self.dataPath):
                raise

        self.print_files()

    def print_files(self):
        files = glob.glob(os.path.join(self.dataPath, '*.sch'))
        i = 1
        for infile in files:
            f = open(infile)
            print "[{}] : {}".format(i, f.read())
            f.close()
            i += 1

    def import_file(self, fpath):
        f = open(fpath)
        ##Do_stuff
        f.close()

    def export_file(self, flag):
        if(flag == "Schedule"):
            fpath = 'out.sch'
        elif(flag == "Task"):
            fpath = 'out.tsk'
        f = open(fpath, "w")
        f.writelines("Output Name")
        ##Do_stuff
        f.close()

    

d = datastruct()