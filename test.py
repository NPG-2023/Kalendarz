import unittest
import datetime
from activity import Activity
from ourCalendar import Calendar


class TestActivity(unittest.TestCase):
    def testCreation(self):
        date1 = datetime.datetime(2023, 4, 3, 18)
        date2 = datetime.datetime(2023, 4, 3, 19)

        with self.assertRaises(ValueError):
            Activity(1, date1, date1)
        with self.assertRaises(ValueError):
            Activity("test", 0, date1)
        with self.assertRaises(ValueError):
            Activity("test", date1, 0)

        activity = Activity("test", date2, date1)

        self.assertEqual(activity.name, "test")
        self.assertEqual(activity.startDate, date1)
        self.assertEqual(activity.endDate, date2)

        with self.assertRaises(ValueError):
            activity.name = 0
        with self.assertRaises(ValueError):
            activity.endDate = "date"
        with self.assertRaises(ValueError):
            activity.startDate = "date"

    def testToString(self):

        date1 = datetime.datetime(2023, 4, 3, 18)
        date2 = datetime.datetime(2023, 4, 3, 19)
        activity = Activity("test", date2, date1)

        self.assertEqual(
            str(activity),
            "test starts At 2023-04-03 18:00:00 and ends at 2023-04-03 19:00:00"
        )


class TestCalendar(unittest.TestCase):

    def testCreation(self):
        with self.assertRaises(ValueError):
            Calendar(1)
        calendar = Calendar("test")

        self.assertEqual(calendar.name, "test")

        with self.assertRaises(ValueError):
            calendar.name = 0

    def testAddActivity(self):
        calendar = Calendar("test")
        activity = Activity(
            "t",
            datetime.datetime(2023, 4, 3, 18),
            datetime.datetime(2023, 4, 3, 19)
        )
        calendar.addActivity(activity)
        self.assertEqual(activity, calendar.activities[0])

    def testActivitiesFromRange(self):
        calendar = Calendar("test")
        activity1 = Activity(
            "t",
            datetime.datetime(2023, 4, 3, 18),
            datetime.datetime(2023, 4, 3, 19)
        )
        activity2 = Activity(
            "t",
            datetime.datetime(2023, 4, 4, 18),
            datetime.datetime(2023, 4, 4, 19)
        )
        calendar.addActivity(activity1)
        calendar.addActivity(activity2)
        inclusive = calendar.getActivitiesFromRange(
            datetime.datetime(2023, 4, 3, 17),
            datetime.datetime(2023, 4, 4, 18, 30),
            True
        )
        self.assertEqual(len(inclusive), 1)
        self.assertEqual(inclusive[0], activity1)
        nonInclusive = calendar.getActivitiesFromRange(
            datetime.datetime(2023, 4, 3, 23),
            datetime.datetime(2023, 4, 4, 18, 30)
        )
        self.assertEqual(len(nonInclusive), 1)
        self.assertEqual(nonInclusive[0], activity2)


if __name__ == "__main__":
    unittest.main()
