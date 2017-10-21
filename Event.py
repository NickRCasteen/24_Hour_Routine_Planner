import pytest




#+++ SUPER CLASS +++
class Event:

	hour1 = 0
	#hour2 = 0
	minute1 = 0
	#minute2 = 0
	timehalf1 = 'AM'
	#timehalf2 = 'AM'
	notification = 0
	
	Calc_Time1 = 0000


	def __init__(self):
		pass

	def ConvertTime(self, hr, mn, th):
		pos_24 = 0000
		#So...start at 12.
		pos_24 = pos_24 + hr*100 #So if hr is 3, it'll make it 0000 -> 0300. If it's 12, then it'll be 1200
		if th == 'PM' and hr != 12:
			#if it's 12 PM, keep it. Otherwise...
			pos_24 = pos_24 + 1200 #If it's 3 PM, then 3+12 = 15, thus 1500.
		if th == 'AM' and hr == 12:
			pos_24 = 0000 #Zero out the hour if it's 12 AM

		pos_24 = pos_24 + mn #No change for minutes. Comes last to avoid hour zeroing.

		return pos_24 #Returns time in 24 hour format

	def ChangeTime(self):
		pass



#+++ SET +++	
class SetEvent(Event):
	def __init__(self, ph1, pm1, pt1, pn):
		self.hour1 = ph1
		self.minute1 = pm1
		self.timehalf1 = pt1
		self.notification = pn
		self.Calc_Time1 = self.ConvertTime(self.hour1, self.minute1, self.timehalf1)

	#CHANGES FOR SET EVENT
	def ChangeTime(self, pnh1, pnm1, pnt1):
		self.hour1 = pnh1
		self.minute1 = pnm1
		self.timehalf1 = pnt1




#+++ RANGE +++
class RangeEvent(Event):
	hour2 = 0
	minute2 = 0
	timehalf2 = 'AM'
	Calc_Time2 = 0

	def __init__(self, ph1, ph2, pm1, pm2, pt1, pt2, pn):
		self.hour1 = ph1
		self.minute1 = pm1
		self.timehalf1 = pt1
		self.notification = pn

		self.Calc_Time1 = self.ConvertTime(self.hour1, self.minute1, self.timehalf1)

		self.hour2 = ph2
		self.minute2 = pm2
		self.timehalf2 = pt2

		self.Calc_Time2 = self.ConvertTime(self.hour2, self.minute2, self.timehalf2)

	def ChangeTime(self, pnh1, pnh2, pnm1, pnm2, pnt1, pnt2):
		self.hour1 = pnh1
		self.minute1 = pnm1
		self.timehalf1 = pnt1
		self.hour2 = pnh2
		self.minute2 = pnm2
		self.timehalf2 = pnt2




# +++ GENERAL +++
class GeneralEvent(Event):
	hour2 = 0
	minute2 = 0
	timehalf2 = 'AM'
	Calc_Time2 = 0

	def __init__(self, ph1, ph2, pm1, pm2, pt1, pt2, pn):
		self.hour1 = ph1
		self.minute1 = pm1
		self.timehalf1 = pt1
		self.notification = pn

		self.Calc_Time1 = self.ConvertTime(self.hour1, self.minute1, self.timehalf1)

		self.hour2 = ph2
		self.minute2 = pm2
		self.timehalf2 = pt2

		self.Calc_Time2 = self.ConvertTime(self.hour2, self.minute2, self.timehalf2)


	def ChangeTime(self, pnh1, pnh2, pnm1, pnm2, pnt1, pnt2):
		self.hour1 = pnh1
		self.minute1 = pnm1
		self.timehalf1 = pnt1
		self.hour2 = pnh2
		self.minute2 = pnm2
		self.timehalf2 = pnt2



#==================================================================================================================================================================
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  ~~  TESTS TO RUN  ~~  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#==================================================================================================================================================================

def test_Event_Creation():
	newThing = SetEvent(5, 55, 'AM', 5) #5:55 AM with notifcation 5
	assert newThing.hour1 == 5
	assert newThing.minute1 == 55
	assert newThing.timehalf1 == 'AM'
	assert newThing.notification == 5
	assert newThing.Calc_Time1 == 555

def test_Range_Event_Creation():
	newThing = RangeEvent(5, 11, 55, 47, 'AM', 'PM', 8) #5:55 AM to 11:47 PM with notifcation 8
	assert newThing.hour1 == 5
	assert newThing.minute1 == 55
	assert newThing.timehalf1 == 'AM'
	assert newThing.notification == 8
	assert newThing.hour2 == 11
	assert newThing.minute2 == 47
	assert newThing.timehalf2 == 'PM'
	assert newThing.Calc_Time2 == 2347

def test_General_Event_Creation():
        newThing = GeneralEvent(12, 11, 22, 47, 'AM', 'PM', 8) #12:22 AM to 11:47 PM with notifcation 8
        assert newThing.hour1 == 12
        assert newThing.minute1 == 22
        assert newThing.timehalf1 == 'AM'
        assert newThing.notification == 8
	assert newThing.Calc_Time1 == 22 #as in 0022
        assert newThing.hour2 == 11
        assert newThing.minute2 == 47
        assert newThing.timehalf2 == 'PM'
        assert newThing.Calc_Time2 == 2347
