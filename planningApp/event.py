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
        self.schedule.deleteEvent(self)
        print("Start Time ")
        self.startTime = self.frontEnd.inputDate()
        print()
        print("End Time ")
        self.endTime = self.frontEnd.inputDate()
        print()
        check = self.schedule.checkConflicts(self)
        if (check):
            self.schedule.addEvent(self)
        return check

    def alert(self):
        now = datetime.now()
        timeToEvent = (self.getStartTime() - now)
        toMinutes = timeToEvent.seconds/60
        hasEnded = (self.getEndTime() - now).seconds < 0
        if toMinutes < (self.getTravelTime() + 5) & hasEnded == False:
            print(self.getTitle() + " will start in " + toMinutes + " minutes")
