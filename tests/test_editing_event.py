
import pytest

from UI import *


def test_view_event():
	Run_Program = ui()
	Run_Program.hour1 = 11
	Run_Program.minute1 = 3
	Run_Program.timehalf1 = "PM"
	Run_Program.notification = 1
	Run_Program.AddEvent()

	assert isinstance(Run_Program.handler.schedule.sched[0],SetEvent)

def test_edit_event():
	Run_Program = ui()
	Run_Program.hour1 = 2
	Run_Program.minute1 = 32
	Run_Program.timehalf1 = "PM"
	Run_Program.notification = 1
	Run_Program.AddEvent()

	Run_Program.handler.Edit(5, 0, 33, 0,'AM','PM', 0, 0) #Goes to event handler

	assert Run_Program.handler.schedule.sched[0].hour1 == 5
	assert Run_Program.handler.schedule.sched[0].minute1 == 33
	assert Run_Program.handler.schedule.sched[0].timehalf1 == 'AM'


pytest.main(['test_editing_event.py'])
