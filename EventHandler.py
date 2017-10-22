#Event Handler class
#TO-DO
from DataStructure import *

class eventhandler(object):

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


	def GetSchedule(self):
		return self.schedule.getSchedule()

	def printTaskFiles(self):
		return self.schedule.print_files(1)

	def printScheduleFiles(self):
		return self.schedule.print_files(0)

	def FileEx(self, scope):
		# Export Schedule
		self.schedule.export_file(scope)

	def FileIm(self, flag, scope):
		files = self.schedule.getFiles(flag)
		self.schedule.import_file(files[int(scope)-1])
