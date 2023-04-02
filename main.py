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
    #makes the fields readonly
    @property
    def name(self):
        return self._name
    
    @property
    def startDate(self):
        return self._startDate
    
    @property
    def endDate(self):
        return self._endDate
    
    #ensures that the types are good
    @name.setter
    def name(self, newName):
        if not type(newName) is str:
            raise ValueError("name is not of type str")
        self._name = newName
    
    @startDate.setter
    def startDate(self,newStartDate):
        if not type(newStartDate) is datetime.datetime:
            raise ValueError("date is not of type datetime.datetime")
        
        self._newStartDate = newStartDate
 
    @endDate.setter
    def endDate(self,newEndDate):
        if not type(newEndDate) is datetime.datetime:
            raise ValueError("date is not of type datetime.datetime")
        
        self._newEndDate = newEndDate

class Calendar:

    def __init__(self, name):
        self.name = name
        self.activities = []

    def addActivity(self,name,date1,date2):
        self.activities.append(Activity(name, date1, date2))

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
    
def main():
    calendar = Calendar("Kalendarz")
    calendar.addActivity("test",datetime.datetime(2023,4,1,20,00),datetime.datetime(2023,4,1,19,00))
    print(calendar)
if __name__ == "__main__":
    main() 