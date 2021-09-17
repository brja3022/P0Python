from frontend import *
from schedule import *
from event import *

print("Welcome to Brian's Planning Application")
name = input("Insert Name ")
print()
schedule = Schedule(name)
frontEnd = FrontEnd()
loop = True
while loop:
    print(
        "Options: 1. Create event, 2. Remove Event, 3. Reschedule Event, 4. View Schedule, 5. Frequent Locations, "
        "6. Quit Application")
    choice = int(input())
    if choice == 1:
        event = frontEnd.create_event(schedule)
        schedule.add_event(event)
    elif choice == 2:
        title = input("Event Title ")
        event = schedule.getEventFromTitle(title)
        schedule.delete_event(event)
        print(title + " has been canceled")
    elif choice == 3:
        title = input("Event Title ")
        event = schedule.getEventFromTitle(title)
        event.reschedule()
        print(title + " has been rescheduled")
    elif choice == 4:
        schedule.printSchedule()
    elif choice == 5:
        print(schedule.frequent_locations())
    elif choice == 6:
        loop = False

    schedule.checkForAlerts()
