from  UI import *

#This will test for being able to add user stories to the schedule.
#The demands will be made in the same order the User is expected to make them. 

Run_Program = ui()

Run_Program.RunMenu() #Will be a tiny test to make sure this component will work. At first will only have one displayed option.

Run_Program.hour1 = 11;
Run_Program.minute1 = 3;
Run_Program.timehalf1 = "PM";
Run_Program.notification = 1;
Run_Program.AddEvent() #Adds an event at 11:03 PM with notification level 1
#Notice we're hard setting the values right here. Much like how the UI will. The user will put in their values and they'll be passed along.

Run_Program.hour1 = 12;
Run_Program.minute1 = 16;
Run_Program.timehalf1 = "AM";
Run_Program.notification = 3;
Run_Program.AddEvent() #And another for 12:16 AM with notification level 3.

Run_Program.hour1 = 32;
Run_Program.minute1 = 22;
Run_Program.timehalf1 = "AM";
Run_Program.notification = 7;
Run_Program.AddEvent() #This should throw an error that hour cannot be >12 and end the attempt to add an event

Run_Program.hour1 = 9;
Run_Program.minute1 = 66;
Run_Program.timehalf1 = "PM";
Run_Program.notification = 2;
Run_Program.AddEvent() #This should throw an error that minute cannot be >60

Run_Program.hour1 = 6;
Run_Program.minute1 = 12;
Run_Program.timehalf1 = "sadsafasf";
Run_Program.notification = 1;
Run_Program.AddEvent() #This should throw an Error that user must specify AM or PM

Run_Program.userinput = "3:54"
Run_Program.timehalf1 = "AM"
Run_Program.ParseTime() #This runs a test for parsing the string into sets of numbers.

Run_Program.userinput = "2:47 AM"
Run_Program.ParseTime() #This should throw an error, stating that AM/PM is not asked for yet.
