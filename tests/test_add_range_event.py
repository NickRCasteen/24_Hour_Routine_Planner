
import pytest


from UI import *




#class UI_test_01:
Run_Program = ui()

def test_add_single_event_correct1():
	Run_Program.hour1 = 11;
	Run_Program.minute1 = 3;
	Run_Program.timehalf1 = "PM";
	Run_Program.notification = 1;
	assert Run_Program.AddEvent() == 1

def test_add_single_event_error():
	Run_Program.hour1 = 32;
	Run_Program.minute1 = 22;
	Run_Program.timehalf1 = "AM";
	Run_Program.notification = 7;
	assert Run_Program.AddEvent() == 0

def test_parser_single_event_correct():
	Run_Program.userinput = "3:54"
	Run_Program.timehalf1 = "AM"
	assert Run_Program.ParseTime(1) == 1 #mode 1
	assert Run_Program.hour1 == 3
	assert Run_Program.minute1 == 54

def test_parser_single_event_error():
	Run_Program.userinput = "2:47 AM"
	assert Run_Program.ParseTime(1) == 0

def test_add_double_evnet_correct():
	Run_Program.hour1 = 12;
	Run_Program.minute1 = 16;
	Run_Program.timehalf1 = "AM";
	Run_Program.notification = 3;
	Run_Program.hour2 = 11;
	Run_Program.minute2 = 10;
	Run_Program.timehalf2 = "PM";
	Run_Program.notification = 3;
	assert Run_Program.AddEvent() == 1

def test_parase_double_event_correct():
	Run_Program.userinput = "3:54"
	Run_Program.timehalf2 = "AM"
	assert Run_Program.ParseTime(2) == 1
	assert Run_Program.hour2 == 3
	assert Run_Program.minute2 == 54


pytest.main(['test_add_range_event.py'])







