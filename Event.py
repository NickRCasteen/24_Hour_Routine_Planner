import pytest


#+++ SET +++	
class SetEvent(object):

        hour1 = 0
        #hour2 = 0
        minute1 = 0
        #minute2 = 0
        timehalf1 = 'AM'
        #timehalf2 = 'AM'
        notification = 0

        hour1_24hr1 = 0

	def __init__(self, ph1, pm1, pt1, pn):
		self.hour1 = ph1
		self.minute1 = pm1
		self.timehalf1 = pt1
		self.notification = pn
		self.hour1_24hr1 = self.ConvertTime(ph1, pt1)


	#CHANGES FOR SET EVENT
	def ChangeTime(self, pnh1, pnm1, pnt1):
		self.hour1 = pnh1
		self.minute1 = pnm1
		self.timehalf1 = pnt1
		self.hour1_24hr1 = self.ConvertTime(pnh1, pnt1)


	def ConvertTime(self, hr, th):
		x = hr
		if th == "PM":
			x = hr + 12

		return x
	

	def toFile(self):
		dlim = '|'
		output = "0"
		output += dlim + str(self.hour1) + dlim + str(self.minute1) + dlim + str(self.timehalf1) + dlim + str(self.notification)
		return output



#+++ RANGE +++
class RangeEvent(object):
	hour1 = 0
	#hour2 = 0
	minute1 = 0
	#minute2 = 0
	timehalf1 = 'AM'
	#timehalf2 = 'AM'
	notification = 0

        hour1_24hr1 = 0
	hour2 = 0
	minute2 = 0
	timehalf2 = 'AM'
	hour1_24hr2 = 0

	def __init__(self, ph1, ph2, pm1, pm2, pt1, pt2, pn):
		self.hour1 = ph1
		self.minute1 = pm1
		self.timehalf1 = pt1
		self.notification = pn

		self.hour1_24hr1 = self.ConvertTime(ph1, pt1)

		self.hour2 = ph2
		self.minute2 = pm2
		self.timehalf2 = pt2

		self.hour1_24hr2 = self.ConvertTime(ph2, pt2)



	def ChangeTime(self, pnh1, pnh2, pnm1, pnm2, pnt1, pnt2):
		self.hour1 = pnh1
		self.minute1 = pnm1
		self.timehalf1 = pnt1

		self.hour1_24hr1 = self.ConvertTime(pnh1, pnt1)

		self.hour2 = pnh2
		self.minute2 = pnm2
		self.timehalf2 = pnt2

		self.hour1_24hr2 = self.ConvertTime(pnh2, pnt2)


	def ConvertTime(self, hr, th):
		x = hr
		if th == "PM":
			x = hr + 12

		return x

	
	def toFile(self):
		dlim = '|'
		output = "1"
		output += dlim + str(self.hour1) + dlim + str(self.hour2) + dlim \
				  + str(self.minute1) + dlim + str(self.minute2) + dlim \
				   + str(self.timehalf1) + dlim + str(self.timehalf2) + dlim \
				  + str(self.notification)
		return output



# +++ GENERAL +++
class GeneralEvent(object):
	hour1 = 0
	#hour2 = 0
	minute1 = 0
	#minute2 = 0
	timehalf1 = 'AM'
	#timehalf2 = 'AM'
	notification = 0

	hour2 = 0
	minute2 = 0
	timehalf2 = 'AM'
	hour1_24hr2 = 0

	def __init__(self, ph1, ph2, pm1, pm2, pt1, pt2, pn):
		self.hour1 = ph1
		self.minute1 = pm1
		self.timehalf1 = pt1
		self.notification = pn

		self.hour1_24hr1 = self.ConvertTime(ph1, pt1)

		self.hour2 = ph2
		self.minute2 = pm2
		self.timehalf2 = pt2

		self.hour1_24hr2 = self.ConvertTime(ph2, pt2)



	def ChangeTime(self, pnh1, pnh2, pnm1, pnm2, pnt1, pnt2):
		self.hour1 = pnh1
		self.minute1 = pnm1
		self.timehalf1 = pnt1

		self.hour1_24hr1 = self.ConvertTime(pnh1, pnt1)

		self.hour2 = pnh2
		self.minute2 = pnm2
		self.timehalf2 = pnt2

		self.hour1_24hr2 = self.ConvertTime(pnh2, pnt2)


	def ConvertTime(self, hr, th):
		x = hr
		if th == "PM":
			x = hr + 12

		return x


	def toFile(self):
		dlim = '|'
		output = "2"
		output += dlim + str(self.hour1) + dlim + str(self.hour2) + dlim \
				  + str(self.minute1) + dlim + str(self.minute2) + dlim \
				  + str(self.timehalf1) + dlim + str(self.timehalf2) + dlim \
				  + str(self.notification)
		return output





#==================================================================================================================================================================
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  ~~  TESTS TO RUN  ~~  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#==================================================================================================================================================================

def test_Event_Creation():
	newThing = SetEvent(5, 55, 'AM', 5) #5:55 AM with notifcation 5
	assert newThing.hour1 == 5
	assert newThing.minute1 == 55
	assert newThing.timehalf1 == 'AM'
	assert newThing.notification == 5

def test_Range_Event_Creation():
	newThing = RangeEvent(5, 11, 55, 47, 'AM', 'PM', 8) #5:55 AM to 11:47 PM with notifcation 8
	assert newThing.hour1 == 5
	assert newThing.minute1 == 55
	assert newThing.timehalf1 == 'AM'
	assert newThing.notification == 8
	assert newThing.hour2 == 11
	assert newThing.minute2 == 47
	assert newThing.timehalf2 == 'PM'

def test_General_Event_Creation():
        newThing = GeneralEvent(12, 11, 22, 47, 'AM', 'PM', 8) #12:22 AM to 11:47 PM with notifcation 8
        assert newThing.hour1 == 12
        assert newThing.minute1 == 22
        assert newThing.timehalf1 == 'AM'
        assert newThing.notification == 8
        assert newThing.hour2 == 11
        assert newThing.minute2 == 47
        assert newThing.timehalf2 == 'PM'
