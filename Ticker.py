
#Okay, how do I WANT this to work?

#I WANT this thing to:
	#Start:
		#Ticker_Time = System_Time + user_defined_offset
	#Loop:
		#Press a key to stop Ticker
		#Show time in 00:00 format
		#Every minute up, iterate through Dataset list to check for notifications.
		#When minute updates when time is 24:59, reset loop
	#Ticker_Time = System_Time + user_defined_offset
		#^ System_Time will be behind Ticker_Time by the offset. So adding the offset will make it 00:00 properly.

import thread

import time

import os

import sys

from EventHandler import *

class clock(object):

	handler_pointer = None
	gen_even_start_min = None
	TimeZone_Offset = 5 #Hardcoded for now. Later should not be hardcoded.

	def __init__(self, parahandler):
		self.handler_pointer = parahandler

#Thanks to the following from Stack Overflow and Stack Exchange for methods:
#Barafu Albino for keyboard interrupt via thread at https://stackoverflow.com/questions/13180941/how-to-kill-a-while-loop-with-a-keystroke
#daviewales for proper usage in the time module at https://codereview.stackexchange.com/questions/26534/is-there-a-better-way-to-count-seconds-in-python
#Vasiliy Rusin for how to clear screen in python at https://stackoverflow.com/questions/2084508/clear-terminal-in-python
#Jrc for how to capture a minute passing https://stackoverflow.com/questions/16000068/python-check-if-a-minute-has-passed



	def input_thread(self,a_list):
		raw_input()
		a_list.append(True)





	def startClock(self, offset=0, timescale=1.0):
		a_list = []
		thread.start_new_thread(self.input_thread, (a_list,))
		os.system('cls||clear') #See if this works.
		lastrun = time.time()

		print "Clock Started. Press any key to stop the clock and return to menu."
		print time.strftime("%I:%M %p")
		#self.PrintTime()
 
		while not a_list:
			Seconds_in_24_Hours = 86400
			#If time.time() is seconds since the Epoch, which started at hour zero, then time.time % Seconds_in_24_Hours will give what part of day
			#We're in.
			if self.minutePassed(time.gmtime(lastrun)[4]):
				#A minute has passed. Check the handler's schedul and re-rpint.
				os.system('cls||clear')
				print "Clock Started. Press any key to stop the clock and return to menu."
				print time.strftime("%I:%M %p")

				self.CheckSchedule() #Look at the whole schedule.
				lastrun = time.time()





	def minutePassed(self, oldminute):
		currentminute = time.gmtime()[4]

		if ((currentminute - oldminute) >= 1) or (oldminute == 59 and currentminute == 0):
			return True
		else:
			return False





	def PrintTime(self):
		hour_print = time.gmtime()[3]
		minute_print = time.gmtime()[4]
		timehalf_print = 'AM'

		if hour_print > 12:
			hour_print = hour_print - 12
			timehalf_print = 'PM'

		print "The Current Time Is: " + str(hour_print) + ":" + str(minute_print) + " " + timehalf_print


	def CheckSchedule(self):
		copy = self.handler_pointer.GetSchedule()
		for i in copy:
			hour_zone = time.gmtime()[3] - self.TimeZone_Offset
			if isinstance(i, SetEvent):
				if i.hour1_24hr1 == hour_zone and i.minute1 == time.gmtime()[4]:
					#Ding! We have a winner!
					self.PrintNotification(i.notification, 1) #Print once
				#return 1

			elif isinstance(i, RangeEvent):
				if i.hour1_24hr1 >= hour_zone and i.minute1 >= time.gmtime()[4]:
					#The Starting Bound
					if i.hour1_24hr2 <= hour_zone and i.minute2 <= time.gmtime()[4]:
						#We're inside the bound.
						self.PrintNotification(i.notification, 2)
				#return 2

			elif isinstance(i, GeneralEvent):
				if i.hour1_24hr1 >= hour_zone and i.minute1 >= time.gmtime()[4]:
					#The Starting Bound
					if i.hour1_24hr2 <= hour_zone and i.minute2 <= time.gmtime()[4]:
						gen_even_start_min = i.minute1 #We're inside the bound, so set the lower.
						#We're inside the bound.
						self.PrintNotification(i.notification, 3)
				#return 3



	def PrintNotification(self, noti, mode):
		#While this middle-man method may seem pointless now, it'll be essential in determining the printing behavior of each class.
		if mode == 1:
			self.passSelection(noti)
		elif mode == 2:
			self.passSelection(noti) #Range Events will continue to notify for the full duration of their effect.
		else:
			self.passSelection(noti) #General Events pop up one minute then return.


	def passSelection(self, notify):
		if notify == 0:
			pass
		elif notify == 1:
			print "Your event for " + str(time.strftime("%I:%M %p")) + " Has begun."
		elif notify == 2:
			print "Please begin your event for " + str(time.strftime("%I:%M %p")) + "."
		elif notify == 3:
			print "It is time to begin your event for " + str(time.strftime("%I:%M %p")) + "."
		elif notify == 4:
			print "Begin your event for " + str(time.strftime("%I:%M %p")) + " now."
		elif notify == 5:
			print "Begin your event for " + str(time.strftime("%I:%M %p")) + " immediately."
		elif notify == 6:
			print "You must start your event for " + str(time.strftime("%I:%M %p")) + " at once."
		elif notify == 7:
			print "Attention. Begin event for " + str(time.strftime("%I:%M %p")) + "."
		elif notify == 8:
			print "URGENT. Begin event for " + str(time.strftime("%I:%M %p")) + "."
		elif notify == 9:
			print "WARNING. YOU MUST START EVENT FOR " + str(time.strftime("%I:%M %p")) + " AT ONCE."





