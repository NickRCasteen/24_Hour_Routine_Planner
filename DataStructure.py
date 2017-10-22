#Data Structures
#TO-DO
import os
import glob
import pytest

from Event import *

class datastruct(object):

    name = "Default Schedule"
    dlim = ":"
    dataPath = 'Data/'
    sched = []  # What will hold all the event objects. Here we define operations for the data.

    def __init__(self):
        try:
            os.makedirs(self.dataPath)
        except OSError:
            if not os.path.isdir(self.dataPath):
                raise

    def getFiles(self, flag):
        if flag == 0:
            return glob.glob(os.path.join(self.dataPath, '*.sch'))
        else:
            return glob.glob(os.path.join(self.dataPath, '*.tsk'))

    def print_files(self, flag):
        files = self.getFiles(flag)
        i = 1
        for infile in files:
            f = open(infile)
            print "[{}] : {}".format(i, f.name)
            f.close()
            i += 1
        return i

    def import_file(self, fpath):
        f = open(fpath)

        input = f.read().split(self.dlim)
        self.name = input.pop(0)
        for s in input:
            ed = s.split("|")
            ty = int(ed.pop(0))
            if ty == 0:
                self.CreateEvent(int(ed.pop(0)), int(ed.pop(0)), ed.pop(0), int(ed.pop(0)))
            elif ty == 1:
                self.CreateEvent2time(int(ed.pop(0)), int(ed.pop(0)), int(ed.pop(0)), int(ed.pop(0)), ed.pop(0), ed.pop(0), int(ed.pop(0)), 0 )
            elif ty == 2:
                self.CreateEvent2time(int(ed.pop(0)), int(ed.pop(0)), int(ed.pop(0)), int(ed.pop(0)), ed.pop(0), ed.pop(0), int(ed.pop(0)), 1)
            else:
                print("ERR: IMPORT" + ty)

        f.close()

    def export_file(self, flag):
        if(flag == 0):
            fpath = self.dataPath + self.name + '.sch'
            f = open(fpath, "w")
            f.write(self.name)

            for sch in self.sched:
                f.write(self.dlim + sch.toFile())

        else:
            fpath = self.dataPath + 'out.tsk'
            f = open(fpath, "w")
            f.write(self.name + self.dlim)
            f.write(self.sched[flag-1].toFile())

        f.close()

    #++CREATE 1
    def CreateEvent(self, dph1, dpm1, dpt1, dpn):
        self.addToSchedule(SetEvent(dph1, dpm1, dpt1, dpn))

	#++CREATE 2
    def CreateEvent2time(self, dph1, dph2, dpm1, dpm2, dpt1, dpt2, dpn, flag):
		if flag == 0:
			self.addToSchedule(RangeEvent(dph1, dph2, dpm1, dpm2, dpt1, dpt2, dpn)) #Flag will be passed in as a means to keep track
		else:
			self.addToSchedule(GeneralEvent(dph1, dph2, dpm1, dpm2, dpt1, dpt2, dpn)) #Flag will be passed in as a means to keep track

	#++ADD TO DATASTRUCTURE LIST
    def addToSchedule(self,a):
        self.sched.append(a) #Add the Event

	#++FOR ACTIVATING TICKER
    def getSchedule(self):
        return self.sched



#d = datastruct()

#==================================================================================================================================================================
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  ~~  TESTS TO RUN  ~~  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#==================================================================================================================================================================

#def test_schedule_type():
	#d = datastruct
	#d.CreateEvent2time(2,3,44,23,'AM','PM',8, 0) #Create Range Event from 2:44 AM to 3:23 PM with notification 8
	#assert type(d.sched[0]) is RangeEvent #The thing we just put in should be a range event
