#Data Structures
#TO-DO
import os
import glob
import pytest
from Event import *

class datastruct:

	sched = [] #What will hold all the event objects. Here we define operations for the data.

	def __init__(self):
		p = 'Data/'

		try:
			os.makedirs(p)
		except OSError:
			if not os.path.isdir(p):
				raise
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


