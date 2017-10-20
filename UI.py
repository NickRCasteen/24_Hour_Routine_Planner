from EventHandler import * 

class ui:

	hour1 = 0
	hour2 = 0
	minute1 = 0
	minute2 = 0
	timehalf1 = 'AM'
	timehalf2 = 'AM'
	notification = 0
	handler = eventhandler()
	userinput = "00:00"

	def __init__(self):
		pass

	def RunMenu(self):
		exit = 1;
		print "Welcome to The 24-Hour-Planner by Team Omicrom Prime.\n Nicholas Casteen\n Jon Paul\n Spencer Graff"

		while exit == 1:
			print "[1] Add Event To Schedule"
			print "[2] Exit"

			userselection = raw_input("Enter Selection\n")

			if userselection == '1':
				self.AESelection()

			elif userselection == '2':
				exit = 0

			else:
				print "Invalid Input."

		return;



#==================================================================================================================================================================
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  ~~  FUNCTION CODE ~~  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#==================================================================================================================================================================

	def AESelection(self):
		self.hour1 = 0
		self.hour2 = 0
		self.minute1 = 0
		self.minute2 = 0
		#TODO: NOTIFICATIONS AT START

		valid = 0
		print "Input the time for this even in 00:00 format (No AM or PM yet)"
		
		while valid == 0:
			self.userinput = raw_input("\n")
			valid = self.ParseTime(1) #Mode 1 is hour/minute 1

		valid = 0
		print "AM or PM?"
		while valid == 0:
			self.timehalf1 = raw_input("\n")
			valid = 1
			if self.timehalf1 != 'AM' and self.timehalf1 != 'PM':
				print "Error. Somehow timehalf not AM or PM."
				valid = 0
		
		valid = 0
		rangchoice = "n"
		print("Make this a range event between two times? y/n?")
		while valid == 0:
			rangchoice = raw_input("\n")
			valid = 1
			if rangchoice != "y" and rangchoice != "n":
				print "Invalid input, y or n only"
				valid = 0

		if rangchoice == "n":
			self.AddEvent() #Pass it in
		else:
			valid = 0
			print "Input the end time for this event in 00:00 format (No AM or PM yet)"
			while valid == 0:
				self.userinput = raw_input("\n")
				valid = self.ParseTime(2) #mode 2 now.

			valid = 0
			print "AM or PM?"
			while valid == 0:
				self.timehalf2 = raw_input("\n")
				valid = 1
				if self.timehalf2 != 'AM' and self.timehalf2 != 'PM':
					print "Error. Somehow timehalf not AM or PM."
					valid = 0

			self.AddEvent() #Pass in what we've done
		

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
			self.handler.Add(self.hour1, self.minute1, self.hour2, self.minute2, self.timehalf1, self.timehalf2, self.notification)
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








