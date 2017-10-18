from EventHandler import * 

class ui:

	hour1 = 0
	hour2 = 0
	minute1 = 0
	minute2 = 0
	timehalf1 = 'AM'
	timehalf1 = 'AM'
	notification = 0
	handler = eventhandler()
	userinput = "00:00"

	def __init__(self):
		pass

	def RunMenu(self):
		print "Welcome to The 24-Hour-Planner by Team Omicrom Prime.\n Nicholas Casteen\n Jon Paul\n Spencer Graff"
		raw_input("press enter")
		return;


#==================================================================================================================================================================
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  ~~  BACKEND TOOLS ~~  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#==================================================================================================================================================================


	def AddEvent(self):
		#Makes checks on the input before passing it to event handler.
		flag = 1
		if self.hour1 < 1 or self.hour1 > 12 or self.minute1 < 0 or self.minute1 > 59:
			flag = 0
			print "Error. Hour over 12? Minute over 59? Aborting."
		if self.timehalf1 != 'AM' and self.timehalf1 != 'PM':
			flag = 0
			print "Error. Somehow timehalf not AM or PM. Aborting."
		if flag == 1:
			self.handler.Add(self.hour1, self.minute1, self.hour2, self.minute2, self.timehalf1, self.notification)
		return;


	def ParseTime(self):
		flag = 0 #Flag for error
		for i in range(len(self.userinput)):
			#Look for semicolon
			if self.userinput[i] == ":":
				self.hour1 = int(self.userinput[:i]) #:i does not include i. Everything before semicolon.
				i = i + 1 #needed because i: does include i
				#perform check for alphanumerics
				for j in self.userinput[i:]:
					if j.isalpha():
						flag = 1 #found an alphanumeric character. Abort.
						break
				if flag == 1:
					break #break early if erorr
				self.minute1 = int(self.userinput[i:]) #No errors, place into minute 1
				break #no need for the rest.

		if flag != 1:
			self.AddEvent() #No errors.

		if flag == 1:
			print "Error. Do not add AM or PM to timestamp."
		return;








