from event import Event

class Schedule:
    def __init__(self, name):
        self.list_events = []
        self.name = name

    def add_event(self, event):
        confirmation = self.check_conflicts(event)
        if confirmation:
            self.list_events.append(event)

    def delete_event(self, event):
        self.list_events.remove(event)

    def check_conflicts(self, event):
        event_cleared = True
        for e in self.list_events:
            new_to_old = event.getStartTime()-e.getEndTime()
            old_to_new = event.getEndTime()-e.getStartTime()
            if (old_to_new.days < 0) | (new_to_old.days > 0):
                continue
            else:
                event_cleared = self.resolve_conflict(event, e)
            if event_cleared == False:
                return event_cleared

        return event_cleared

    def resolve_conflict(self, new_event, old_event):
        event_cleared = False
        print(new_event.getTitle() + " and " + old_event.getTitle() + "occur at overlapping times. How would you like "
                                                                      "to resolve this conflict?")
        print("1. Reschedule " + new_event.getTitle())
        print("2. Reschedule " + old_event.getTitle())
        print("3. Keep both events at this time")
        print("4. Cancel " + new_event.getTitle())
        choice = int(input())
        if choice == 1:
            event_cleared = new_event.reschedule()
        elif choice == 2:
            event_cleared = old_event.reschedule()
        elif choice == 3:
            event_cleared = True
        elif choice == 4:
            event_cleared = False
        else:
            event_cleared = False

        return event_cleared

    def frequent_locations(self):
        commonLocations = []
        for event in self.list_events:
            if event.getLocation() in commonLocations:
                for (index, location, frequency) in commonLocations:
                    if location == event.getLocation():
                        break
                commonLocations[index] = (event.getLocation(), frequency + 1)
            else:
                commonLocations.append((event.getLocation(), 1))

        return commonLocations

    def printSchedule(self):
        print(self.name + "Schedule")
        for event in self.list_events:
            print(f"{event.getTitle()} Starts: {event.getStartTime()} Ends: {event.getEndTime()} Location: {event.getLocation()}")

    def getEventFromTitle(self, title):
        returnable = None
        for event in self.list_events:
            if event.getTitle() == title:
                returnable = event

        return returnable

    def checkForAlerts(self):

        for event in self.list_events:
            event.alert()
