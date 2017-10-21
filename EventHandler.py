#Event Handler class
#TO-DO
from DataStructure import *

class eventhandler:

	schedule = datastruct()

	def __init__(self):
		pass

	def Add(self, hr1, hr2, mt1, mt2, half1, half2, notify_level, flag):
		if hr2 != 0:
			self.schedule.CreateEvent2time(hr1, hr2, mt1, mt2, half1, half2, notify_level, flag) 
			#This is a range event or a general event, based on the flag. It doesn't matter, data struct takes care of it.
		else:
			self.schedule.CreateEvent(hr1, mt1, half1, notify_level)
			#Here, we need only pass in the parameters for a singular event. More buck-passing.

	def Edit(self, hr1, hr2, mt1, mt2, half1, half2, flag, index):
		if flag == 0:
			self.schedule.sched[index].ChangeTime(hr1, mt1, half1)

		if flag == 1:
			self.schedule.sched[index].ChangeTime(hr1, hr2, mt1, mt2, half1, half2)
