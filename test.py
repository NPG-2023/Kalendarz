import unittest
from datetime import datetime
from activity import Activity
from ourCalendar import Calendar
import os


class TestActivity(unittest.TestCase):
    def test_creation(self):
        date1 = datetime(2023, 4, 3, 18)
        date2 = datetime(2023, 4, 3, 19)

        activity = Activity("test", "test", date2, date1)

        self.assertEqual(activity.name, "test")
        self.assertEqual(activity.place, "test")
        self.assertEqual(activity.start_date, date1)
        self.assertEqual(activity.end_date, date2)

    def test_to_string(self):

        date1 = datetime(2023, 4, 3, 18)
        date2 = datetime(2023, 4, 3, 19)
        activity = Activity("test", "test", date2, date1)

        self.assertEqual(
            str(activity),
            "test miejsce: test zaczyna się: 2023-04-03 18:00:00 i kończy: 2023-04-03 19:00:00"
        )

    def test_to_file_format(self):

        date1 = datetime(2023, 4, 3, 18)
        date2 = datetime(2023, 4, 3, 19)
        activity = Activity("test", "test", date2, date1)

        self.assertEqual(
            activity.to_file_format(),
            "test test 1680537600.0 1680541200.0"
        )

    def test_from_file_format(self):
        with self.assertRaises(ValueError):
            Activity.from_file_format("NotAValidFormat")

        activity = Activity.from_file_format(
            "test test 1680537600.0 1680541200.0")
        date1 = datetime(2023, 4, 3, 18)
        date2 = datetime(2023, 4, 3, 19)

        self.assertEqual(activity.name, "test")
        self.assertEqual(activity.place, "test")
        self.assertEqual(activity.start_date, date1)
        self.assertEqual(activity.end_date, date2)


class TestCalendar(unittest.TestCase):

    def test_creation(self):
        calendar = Calendar("", "test")
        self.assertEqual(calendar.name, "test")

    def test_add_activity(self):
        calendar = Calendar("", "test")
        activity = Activity(
            "t",
            "t",
            datetime(2023, 4, 3, 18),
            datetime(2023, 4, 3, 19)
        )
        calendar.add_activity(activity)
        self.assertEqual(activity, calendar.activities[0])

    def test_remove_activity(self):
        calendar = Calendar("", "test")
        activity = Activity(
            "t",
            "t",
            datetime(2023, 4, 3, 18),
            datetime(2023, 4, 3, 19)
        )
        calendar.add_activity(activity)
        self.assertEqual(True, activity in calendar.activities)

        calendar.remove_activity(activity)
        self.assertEqual(False, activity in calendar.activities)

    def test_edit_name_activity(self):
        calendar = Calendar("", "test")
        activity = Activity(
            "t",
            "t",
            datetime(2023, 4, 3, 18),
            datetime(2023, 4, 3, 19)
        )
        calendar.add_activity(activity)
        calendar.change_activity_name(activity, "new name")
        self.assertEqual("new name", calendar.activities[0].name)

    def test_edit_place_activity(self):
        calendar = Calendar("", "test")
        activity = Activity(
            "t",
            "t2",
            datetime(2023, 4, 3, 18),
            datetime(2023, 4, 3, 19)
        )
        calendar.add_activity(activity)
        calendar.change_activity_place(activity, "new place")
        self.assertEqual("new place", calendar.activities[0].place)

    def test_edit_date_activity(self):
        calendar = Calendar("", "test")
        activity = Activity(
            "t",
            "t",
            datetime(2023, 4, 3, 18),
            datetime(2023, 4, 3, 19)
        )
        calendar.add_activity(activity)
        d1 = datetime(2023, 5, 3, 18)
        d2 = datetime(2023, 6, 3, 18)
        calendar.change_activity_dates(activity, d1, d2)
        self.assertEqual(d1, calendar.activities[0].start_date)
        self.assertEqual(d2, calendar.activities[0].end_date)

    def test_activities_from_range(self):
        calendar = Calendar("", "test")
        activity1 = Activity(
            "t",
            "t",
            datetime(2023, 4, 3, 18),
            datetime(2023, 4, 3, 19)
        )
        activity2 = Activity(
            "t",
            "t",
            datetime(2023, 4, 4, 18),
            datetime(2023, 4, 4, 19)
        )
        calendar.add_activity(activity1)
        calendar.add_activity(activity2)
        inclusive = calendar.get_activities_from_range(
            datetime(2023, 4, 3, 17),
            datetime(2023, 4, 4, 18, 30),
            True
        )
        self.assertEqual(len(inclusive), 1)
        self.assertEqual(inclusive[0], activity1)
        non_inclusive = calendar.get_activities_from_range(
            datetime(2023, 4, 3, 23),
            datetime(2023, 4, 4, 18, 30)
        )
        self.assertEqual(len(non_inclusive), 1)
        self.assertEqual(non_inclusive[0], activity2)

    def test_to_file_format(self):

        cal = Calendar("", "test")

        date1 = datetime(2023, 4, 3, 18)
        date2 = datetime(2023, 4, 3, 19)
        cal.add_activity(Activity("test", "test", date2, date1))

        self.assertEqual(
            cal.to_file_format(),
            "test"
            "\ntest test 1680537600.0 1680541200.0"""
        )

    def test_from_file_format(self):

        cal = Calendar.from_file_format(
            "test"
            "\ntest test 1680537600.0 1680541200.0"
        )

        self.assertEqual(cal.name, "test")
        self.assertEqual(len(cal.activities), 1)
        self.assertEqual(cal.activities[0].name, "test")

    def test_save_and_load_from_file(self):
        cal = Calendar("", "test")
        date1 = datetime(2023, 4, 3, 18)
        date2 = datetime(2023, 4, 3, 19)
        activity = Activity("activity", "test", date1, date2)
        cal.add_activity(activity)

        cal.save_to_file("./testCalendarSaveAndLoadFromFile.txt")
        cal2 = Calendar.load_from_file("./testCalendarSaveAndLoadFromFile.txt")

        self.assertEqual(cal.name, cal2.name)
        self.assertEqual(len(cal.activities), len(cal2.activities))
        self.assertEqual(cal.activities[0].name, cal2.activities[0].name)

        os.remove("./testCalendarSaveAndLoadFromFile.txt")

    def test_automatic_load_and_save(self):
        with open("./testCalendarAutomaticLoadAndSave", 'w') as file:
            file.write(
                "test"
                "\ntest test 1680537600.0 1680541200.0"
            )
        cal = Calendar("./testCalendarAutomaticLoadAndSave")
        self.assertEqual("test", cal.name)
        self.assertEqual("test", cal.activities[0].name)
        cal.name = "test2"
        cal.activities[0].name = "test3"
        del cal
        with open("./testCalendarAutomaticLoadAndSave", 'r') as file:
            self.assertEqual(
                "test2"
                "\ntest3 test 1680537600.0 1680541200.0",
                file.read()
            )
        os.remove("./testCalendarAutomaticLoadAndSave")


if __name__ == "__main__":
    unittest.main()
