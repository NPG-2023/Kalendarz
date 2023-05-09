# this file name is strange because calendar is taken by python standard library
import datetime
from activity import Activity


class Calendar:

    def __init__(self, name):
        if not type(name) is str:
            raise ValueError("name is not of type str")
        self.name = name
        self.activities = []

    def addActivity(self, activity):
        self.activities.append(activity)

    def __str__(self):
        activitiesStr = ""
        for act in self.activities:
            activitiesStr += str(act) + "\n"
        return f"{self.name} has following activities:\n{activitiesStr}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newName):
        if not type(newName) is str:
            raise ValueError("name is not of type str")
        self._name = newName

    def getActivitiesFromRange(self, start, end, onlyInclusion=False):
        if not (type(start) is datetime.datetime and type(end) is datetime.datetime):
            raise ValueError("dates are not of type datetime.datetime")
        res = []
        for activity in self.activities:
            if onlyInclusion:
                if activity.startDate > start and activity.endDate < end:
                    res.append(activity)
            else:
                if activity.endDate > start and activity.startDate < end:
                    res.append(activity)
        return res

    def toFileFormat(self):
        contents = f"{self.name}"
        for activity in self.activities:
            contents += "\n" + activity.toFileFormat()
        return contents

    @staticmethod
    def fromFileFormat(contents):
        data = contents.split("\n")
        cal = Calendar(data[0])
        for actStr in data[1:]:
            cal.addActivity(Activity.fromFileFormat(actStr))
        return cal

    def saveToFile(self, path):
        with open(path, 'w') as file:
            file.write(self.toFileFormat())

    @staticmethod
    def loadFromFile(path):
        with open(path, 'r') as file:
            return Calendar.fromFileFormat(file.read())
