# this file name is strange because calendar is taken by python standard library
from datetime import datetime
from activity import Activity
from typing import List
import os


class Calendar:

    def __init__(self, path: str, name: str = "Kalendarz"):
        self.path = path

        if os.path.isfile(path):
            cal = Calendar.load_from_file(path)
            self.name = cal.name
            self.activities = cal.activities
        else:
            self.name = name
            self.activities = []

    def __del__(self):
        if not self.path:
            return
        self.save_to_file(self.path)

    def add_activity(self, activity: Activity):
        self.activities.append(activity)

    def remove_activity(self, activity: Activity):
        if activity in self.activities:
            self.activities.remove(activity)

    def change_activity_dates(self, activity: Activity, hour: str):
        if activity in self.activities:
            activity.hour = hour
        else:
            raise LookupError("activity is not in a calendar")

    def change_activity_name(self, activity: Activity, new_name: str):
        if activity in self.activities:
            activity.name = new_name
        else:
            raise LookupError("activity is not in a calendar")

    def __str__(self) -> str:
        activities_str = ""
        for act in self.activities:
            activities_str += str(act) + "\n"
        return f"{self.name} has following activities:\n{activities_str}"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    def get_activities_from_range(self, start: datetime, end: datetime, only_inclusion: bool = False) -> List[Activity]:
        res = []
        for activity in self.activities:
            if only_inclusion:
                if activity.start_date >= start and activity.end_date <= end:
                    res.append(activity)
            else:
                if activity.end_date >= start and activity.start_date <= end:
                    res.append(activity)
        return res

    def to_file_format(self):
        contents = f"{self.name}"
        for activity in self.activities:
            contents += "\n" + activity.to_file_format()
        return contents

    @classmethod
    def from_file_format(cls, contents: str):
        data = contents.split("\n")
        cal = cls("", data[0])
        for act_str in data[1:]:
            cal.add_activity(Activity.from_file_format(act_str))
        return cal

    def save_to_file(self, path: str):
        with open(path, 'w') as file:
            file.write(self.to_file_format())

    @classmethod
    def load_from_file(cls, path: str):
        with open(path, 'r') as file:
            return cls.from_file_format(file.read())
