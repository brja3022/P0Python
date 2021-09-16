from datetime import datetime
from schedule import *
from frontend import *


class Event:
    def __init__(self, eventTitle, eventStartTime, eventEndTime, eventLocation, eventTravelTime, schedule, frontEnd):
        self.title = eventTitle
        self.startTime = eventStartTime
        self.endTime = eventEndTime
        self.location = eventLocation
        self.travelTime = eventTravelTime
        self.schedule = schedule
        self.frontEnd = frontEnd

    def getTitle(self):
        return self.title

    def getStartTime(self):
        return self.startTime

    def getEndTime(self):
        return self.endTime

    def getLocation(self):
        return self.location

    def getTravelTime(self):
        return self.travelTime

    def reschedule(self):
        self.schedule.delete_event(self)
        print("Start Time ")
        self.startTime = self.frontEnd.input_date()
        print()
        print("End Time ")
        self.endTime = self.frontEnd.input_date()
        print()
        check = self.schedule.check_conflicts(self)
        if check:
            self.schedule.add_event(self)
        return check

    def alert(self):
        now = datetime.now()
        timeToEvent = (self.getStartTime() - now)
        toMinutes = round(timeToEvent.seconds / 60)
        hasEnded = (self.getEndTime() - now).seconds < 0
        if (timeToEvent.days < 1) & (toMinutes < (self.getTravelTime() + 5)) & (hasEnded == False):
            print(f"{self.getTitle()} will start in {toMinutes} minutes")
