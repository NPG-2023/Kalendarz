import datetime


class Activity:

    def __init__(self, name, date1, date2):
        if not (type(date1) is datetime.datetime and type(date2) is datetime.datetime):
            raise ValueError("dates are not of type datetime.datetime")
        if not type(name) is str:
            raise ValueError("name is not of type string")
        if date1 > date2:
            self._endDate = date1
            self._startDate = date2
        else:
            self._endDate = date2
            self._startDate = date1

        self._name = name

    def __str__(self):
        return f"{self.name} starts At {self.startDate} and ends at {self.endDate}"
    # makes the fields readonly

    def toFileFormat(self):
        return f"{self.name} {self.startDate.timestamp()} {self.endDate.timestamp()}"

    @staticmethod
    def fromFileFormat(str):
        data = str.split(' ')
        if len(data) != 3:
            raise ValueError("data is not formatted correctly")
        name = data[0]
        startTimestamp = datetime.datetime.fromtimestamp(float(data[1]))
        endTimestamp = datetime.datetime.fromtimestamp(float(data[2]))
        return Activity(name, startTimestamp, endTimestamp)

    @property
    def name(self):
        return self._name

    @property
    def startDate(self):
        return self._startDate

    @property
    def endDate(self):
        return self._endDate

    # ensures that the types are good
    @name.setter
    def name(self, newName):
        if not type(newName) is str:
            raise ValueError("name is not of type str")
        self._name = newName

    @startDate.setter
    def startDate(self, newStartDate):
        if not type(newStartDate) is datetime.datetime:
            raise ValueError("date is not of type datetime.datetime")

        self._newStartDate = newStartDate

    @endDate.setter
    def endDate(self, newEndDate):
        if not type(newEndDate) is datetime.datetime:
            raise ValueError("date is not of type datetime.datetime")

        self._newEndDate = newEndDate
