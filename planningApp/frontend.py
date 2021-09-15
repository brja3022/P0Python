from datetime import datetime
from schedule import *
from event import *


class FrontEnd:

    def input_date(self):
        year = int(input("year"))
        month = int(input("month"))
        day = int(input("day"))
        hour = int(input("hour"))
        minute = int(input("minute"))
        #date_time_str = input("Input date in format dd/mm/yyyy HH:MM:SS ")
        #date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')
        date_time_obj = datetime(year, month, day, hour, minute)
        return date_time_obj

    def create_event(self, schedule):
        title = input("Event Title ")
        print("Start Date/Time ")
        start = self.input_date()
        print("End Date/Time ")
        end = self.input_date()
        location = input("Event Location ")
        print("Travel Time in minutes ")
        tt = int(input())
        return Event(title, start, end, location, tt, schedule, self)
