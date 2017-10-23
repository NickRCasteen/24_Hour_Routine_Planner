from EventHandler import * 
from Ticker import *


class ui(object):

	hour1 = 0 #Info to pass in
	hour2 = 0 #Info to pass in
	minute1 = 0 #Info to pass in
	minute2 = 0 #Info to pass in
	timehalf1 = 'AM' #Time half 1
	timehalf2 = 'AM' #Time half 2
	notification = 0 #The notification level to pass in
	handler = eventhandler() #The Event Handler Object this class will call to perform its operations.
	userinput = "00:00" #A string input from the user for the time, to be parsed into hour/minute values
	RangeGenFlag = 0 #A flag for distinguishing between range events and general events

	def __init__(self):
		pass

	def RunMenu(self):
		exit = 1;
		print "Welcome to The 24-Hour-Planner by Team Omicrom Prime.\n Nicholas Casteen\n John Lee\n Spencer Graff"

		while exit == 1:
			print "[1] Add Event To Schedule"
			print "[2] Edit a Node"
			print "[3] Begin Clock"
			print "[4] Set task to completed"
			print "[8] Export to file"
			print "[9] Import from file"
			print "[0] Exit"

			userselection = raw_input("Enter Selection\n")

			if userselection == '1':
				self.AESelection() #Add it
				self.AddEvent() #Put it in here, just to reduce nested methods

			elif userselection == '2':
				self.EESelection()
			elif userselection == '3':
				clockobj = clock(self.handler)
				clockobj.startClock()

			# Export
			elif userselection == '8':
				self.ExSelection()
			# Import
			elif userselection == '9':
				self.ImSelection()

			elif userselection == '0':
				exit = 0

			else:
				print "Invalid Input."

		return;



#==================================================================================================================================================================
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  ~~  FUNCTION CODE ~~  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#==================================================================================================================================================================
	#SELECTION ONE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
	def AESelection(self):
		self.hour1 = 0
		self.hour2 = 0
		self.minute1 = 0
		self.minute2 = 0
		

		#NOTIFICATIONS
		valid = 0
		print "What is the notification level for this event, 0 to 9, 0 = Don't Notify / 9 = Maximum Level"
		while valid == 0:
			noti_string = raw_input("\n")
			valid = 1
			for i in noti_string:
				if i.isalpha():
					valid = 0 #Check for if what was inputted was a number or not
			if valid == 1:
				self.notification = int(noti_string)
				if self.notification > 9:
					valid = 0 #A check to make sure they only input 0 through 9
					print "Numbers 0 to 9 only"
			else:
				print "Invalid input, numbers only."


		#TIME FOR FIRST BOUND
		valid = 0
		print "Input the time for this even in 00:00 format (No AM or PM yet)"
		while valid == 0:
			self.userinput = raw_input("\n")
			valid = self.ParseTime(1) #Mode 1 is hour/minute 1. Returns 1 or 0.


		#AM OR PM FOR FIRST BOUND
		valid = 0
		print "AM or PM?"
		while valid == 0:
			self.timehalf1 = raw_input("\n")
			valid = 1
			if self.timehalf1 != 'AM' and self.timehalf1 != 'PM':
				print "Error. Somehow timehalf not AM or PM."
				valid = 0


		#RANGE OR NOT?
		valid = 0
		rangchoice = "n"
		print("Make this a range event between two times? y/n?")
		while valid == 0:
			rangchoice = raw_input("\n")
			valid = 1
			if rangchoice != "y" and rangchoice != "n":
				print "Invalid input, y or n only"
				valid = 0



		#SETTING HOURS, MINUTES AND TIMEHALF FOR RANGE'S END BOUND
		if rangchoice == "n":
			return 1 #Pass it in
		else:
			valid = 0 #Begin with check for range event or general event
			print "Shall this event continiously notify you? y/n"
			while valid == 0:
				rangtypechoice = raw_input("\n")
				valid = 1
				if rangtypechoice != "y" and rangtypechoice != "n":
					valid = 0
					print "y or n only"
				if valid == 1:
					if rangtypechoice == "y":
						self.RangeGenFlag = 0 #Flag = 0 results in range event
					else:
						self.RangeGenFlag = 1

			valid = 0 #Next, time for lower range, parse for hour and minute
			print "Input the end time for this event in 00:00 format (No AM or PM yet)"
			while valid == 0:
				self.userinput = raw_input("\n")
				valid = self.ParseTime(2) #mode 2 now.


			valid = 0 #AM or PM
			print "AM or PM?"
			while valid == 0:
				self.timehalf2 = raw_input("\n")
				valid = 1
				if self.timehalf2 != 'AM' and self.timehalf2 != 'PM':
					print "Error. Somehow timehalf not AM or PM."
					valid = 0


			return 1 #Pass in what we've done




	#SELECTION TWO <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
	def EESelection(self):
		valid = 0
		EventIndex = 0
		self.hour1 = 0
		self.hour2 = 0
		self.minute1 = 0
		self.minute2 = 0


		print "Which Event would you like to edit?"
		self.PrintEventsInScehdule()
		while valid == 0:
			choiceinput = raw_input("\n")
			valid = 1
			for i in choiceinput:
				if i.isalpha():
					print "Invalid Input. Numerical selection only."
					valid = 0
			if valid == 1:
				EventIndex = int(choiceinput)

		print "What would you like to change?"
		print "[0] Time"

		valid = 0
		while valid == 0:
			choiceinput = raw_input("\n")
			valid = 1
			for i in choiceinput:
				if i.isalpha():
					print "Invalid Input. Numerical selection only."
					valid = 0
				if valid == 1:
					if int(choiceinput) < 0 or int(choiceinput) > 0:
						print "Inputs from 0 to 0 only"
						valid = 0 #TODO: THIS IS TEMPORARY. AS FEATURES ARE ADDED THESE RANGES MUST CHAMGE.

		#CHOICE TO ALTER TIME
		if choiceinput == "0":
			#Check type
			valid = 0
			print "Type the new time in 00:00 format, no AM/PM yet."
			while valid == 0:
				self.userinput = raw_input("\n")
				valid = self.ParseTime(1) #We're going to set the hour and such again.
			valid = 0
			print "AM or PM?"
			while valid == 0:
				self.timehalf1 = raw_input("\n")
				valid = 1
				if self.timehalf1 != 'AM' and self.timehalf1 != 'PM':
					print "Error. Somehow timehalf not AM or PM."
					valid = 0

			if isinstance(self.handler.schedule.sched[EventIndex],SetEvent): #This to handler to dataset to dataset's list
				self.handler.Edit(self.hour1, self.minute1, self.timehalf1,0,0,'PM',0,EventIndex) #SLot it straight it.

			else:
				print "Type the new ending time in 00:00 format, no AM/PM yet."
				valid = 0
				while valid == 0:
					self.userinput = raw_input("\n")
					valid = self.ParseTime(2) #We're going to set the hour and such again.
				valid = 0
				print "AM or PM?"
				while valid == 0:
					self.timehalf2 = raw_input("\n")
					valid = 1
					if self.timehalf2 != 'AM' and self.timehalf2 != 'PM':
						print "Error. Somehow timehalf not AM or PM."
						valid = 0

				self.handler.Edit(self.hour1,self.hour2,self.minute1,self.minute2,self.timehalf1,self.timehalf2,1,EventIndex)

	def ExSelection(self):
		valid = 0
		intxt = ""

		print "Schedule or Task?"

		while valid == 0:
			intxt = raw_input("\n")
			valid = 1
			if intxt != 'Schedule' and intxt != 'Task':
				print "Error. Bad input"
				valid = 0
		valid = 0

		if intxt == "Task":
			while valid == 0:
				self.PrintEventsInScehdule()
				intxt = raw_input("\n")
				valid = 1
				if int(intxt) > len(self.handler.schedule.sched):
					print "Error. Index too large"
					valid = 0
				valid = 0
			self.handler.FileEx(int(intxt))
		else:
			self.handler.FileEx(0)

	def ImSelection(self):
		valid = 0
		intxt = ""

		print "Schedule or Task?"

		while valid == 0:
			intxt = raw_input("\n")
			valid = 1
			if intxt != 'Schedule' and intxt != 'Task':
				print "Error. Bad input"
				valid = 0
		valid = 0

		print "Select a file"
		if intxt == "Task":
			nTask = self.handler.printTaskFiles()
			while valid == 0:
				intxt = raw_input("\n")
				valid = 1
				if int(intxt) > nTask:
					print "Error. Bad index"
					valid = 0
			self.handler.FileIm(1, intxt)

		else:
			nSch = self.handler.printScheduleFiles()
			while valid == 0:
				intxt = raw_input("\n")
				valid = 1
				if int(intxt) > nSch:
					print "Error. Bad index"
					valid = 0
			self.handler.FileIm(0, intxt)
		
#==================================================================================================================================================================
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  ~~  BACKEND TOOLS ~~  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#==================================================================================================================================================================



	def AddEvent(self):
		#Makes checks on the input before passing it to event handler.
		flag = 1
		if self.hour1 < 1 or self.hour1 > 12 or self.minute1 < 0 or self.minute1 > 59:
			flag = 0
			print "Error. Hour over 12? Minute over 59? Aborting."
		if self.hour2 > 12 or self.minute2 < 0 or self.minute2 > 59:
			flag = 0
			print "Error. Second set incorrect."
		if self.timehalf1 != 'AM' and self.timehalf1 != 'PM':
			flag = 0
			print "Error. Somehow timehalf not AM or PM. Aborting."
		if flag == 1:
			self.handler.Add(self.hour1, self.hour2, self.minute1, self.minute2, self.timehalf1, self.timehalf2, self.notification, self.RangeGenFlag)
			return 1
		return 0




	def ParseTime(self, mode):
		flag = 0 #Flag for error
		for i in range(len(self.userinput)):
			#Look for semicolon
			if self.userinput[i] == ":":

				#HOURS PARSER
				if mode == 1:
					self.hour1 = int(self.userinput[:i]) #:i does not include i. Everything before semicolon.
				else:
					self.hour2 = int(self.userinput[:i])

				i = i + 1 #needed because i: does include i
				#perform check for alphanumerics
				for j in self.userinput[i:]:
					if j.isalpha():
						flag = 1 #found an alphanumeric character. Abort.
						break
				if flag == 1:
					break #break early if erorr


				#MINUTES PARSER
				if mode == 1:
					self.minute1 = int(self.userinput[i:]) #No errors, place into minute 1
				else:
					self.minute2 = int(self.userinput[i:])


				break #no need for the rest.

		if flag == 1:
			print "Error. Do not add AM or PM to timestamp."
			if mode == 1:
				self.hour1 = 0
			else:
				self.hour2 = 0
			return 0; #Return with error to loop.

		return 1; #Return ok




	def PrintEventsInScehdule(self):
		#for i in (self.handler.schedule.sched)
			#print (str(i.hour1) + str(i.minute1)
		pass


	def completedEvent(self):
		if 1 == 1:
			print("The event is completed")
		else:
			print("This event is not completed")




#==================================================================================================================================================================
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  ~~  TESTS TO RUN  ~~  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#==================================================================================================================================================================

def test_add_single_event_correct1():
	Run_Program = ui()
	Run_Program.hour1 = 11
	Run_Program.minute1 = 3
	Run_Program.timehalf1 = "PM"
	Run_Program.notification = 1
	assert Run_Program.AddEvent() == 1

def test_add_single_event_error():
	Run_Program = ui()
	Run_Program.hour1 = 32
	Run_Program.minute1 = 22
	Run_Program.timehalf1 = "AM"
	Run_Program.notification = 7
	assert Run_Program.AddEvent() == 0

def test_parser_single_event_correct():
	Run_Program = ui()
	Run_Program.userinput = "3:54"
	Run_Program.timehalf1 = "AM"
	assert Run_Program.ParseTime(1) == 1 #mode 1
	assert Run_Program.hour1 == 3
	assert Run_Program.minute1 == 54

def test_parser_single_event_error():
	Run_Program = ui()
	Run_Program.userinput = "2:47 AM"
	assert Run_Program.ParseTime(1) == 0

def test_add_double_evnet_correct():
	Run_Program = ui()
	Run_Program.hour1 = 12
	Run_Program.minute1 = 16
	Run_Program.timehalf1 = "AM"
	Run_Program.notification = 3
	Run_Program.hour2 = 11
	Run_Program.minute2 = 10
	Run_Program.timehalf2 = "PM"
	Run_Program.notification = 3
	assert Run_Program.AddEvent() == 1

def test_parase_double_event_correct():
	Run_Program = ui()
	Run_Program.userinput = "3:54"
	Run_Program.timehalf2 = "AM"
	assert Run_Program.ParseTime(2) == 1
	assert Run_Program.hour2 == 3
	assert Run_Program.minute2 == 54
	
