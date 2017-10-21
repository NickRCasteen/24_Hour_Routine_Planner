
import pytest

from Event import *

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

pytest.main(['test_Event_Class.py'])
