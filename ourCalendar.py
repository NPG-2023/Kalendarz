# this file name is strange because calendar is taken by python standard library
from datetime import datetime, timedelta
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

    def change_activity_dates(self, activity: Activity, new_start_date: datetime, new_end_date: datetime):
        if activity in self.activities:
            activity.start_date = new_start_date
            activity.end_date = new_end_date
        else:
            raise LookupError("activity is not in a calendar")

    def change_activity_place(self, activity: Activity, new_place: str):
        if activity in self.activities:
            activity.place = new_place
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

    # Lista polskich świąt
    POLISH_HOLIDAYS = {
        "Nowy Rok": (1, 1),
        "Trzech Króli": (6, 1),
        "Wielkanoc": None,
        "Poniedziałek Wielkanocny": None,
        "Święto Pracy": (1, 5),
        "Święto Konstytucji 3 Maja": (3, 5),
        "Boże Ciało": None,
        "Święto Wojska Polskiego": (15, 8),
        "Wniebowzięcie Najświętszej Maryi Panny": (15, 8),
        "Wszystkich Świętych": (1, 11),
        "Narodowe Święto Niepodległości": (11, 11),
        "Boże Narodzenie": (25, 12),
    }


    def get_polish_holidays(self, year: int) -> List[Activity]:
        polish_holidays = []
        for name, date in self.POLISH_HOLIDAYS.items():
            if date is None:
                date = self.calculate_holiday_date(year, name)
            activity = Activity(name, date, date)
            polish_holidays.append(activity)
        return polish_holidays

    def calculate_holiday_date(self, year: int, holiday_name: str) -> datetime:
        if holiday_name == "Wielkanoc":
            return self.calculate_easter_date(year)
        elif holiday_name == "Poniedziałek Wielkanocny":
            easter_date = self.calculate_easter_date(year)
            return easter_date + timedelta(days=1)
        elif holiday_name == "Boże Ciało":
            easter_date = self.calculate_easter_date(year)
            return easter_date + timedelta(days=60)
        else:
            raise ValueError("Nieznane święto: " + holiday_name)

    def calculate_easter_date(self, year: int) -> datetime:
        #wyznaczenie daty wielkanocy za pomocą algorytmu Gaussa
        a = year % 19
        b = year // 100
        c = year % 100
        d = b // 4
        e = b % 4
        f = (b + 8) // 25
        g = (b - f + 1) // 3
        h = (19 * a + b - d - g + 15) % 30
        i = c // 4
        k = c % 4
        l = (32 + 2 * e + 2 * i - h - k) % 7
        m = (a + 11 * h + 22 * l) // 451
        month = (h + l - 7 * m + 114) // 31
        day = ((h + l - 7 * m + 114) % 31) + 1
        return datetime(year, month, day)

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





