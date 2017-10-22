#Data Structures
#TO-DO
import os
import glob
import pytest
from Event import *

class datastruct:
    dataPath = 'Data/'
    sched = []  # What will hold all the event objects. Here we define operations for the data.

    def __init__(self):
        try:
            os.makedirs(self.dataPath)
        except OSError:
            if not os.path.isdir(self.dataPath):
                raise

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
