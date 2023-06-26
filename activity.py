from datetime import datetime


class Activity:

    def __init__(self, name: str, date1: datetime, date2: datetime, hour: str):
        if date1 > date2:
            self._end_date = date1
            self._start_date = date2
            self._hour = None
        else:
            self._end_date = date2
            self._start_date = date1

        self._name = name

    def __str__(self) -> str:
        return f"{self.name} starts At {self.start_date} and ends at {self.end_date}"
    # makes the fields readonly

    def to_file_format(self) -> str:
        return f"{self.name} {self.start_date.timestamp()} {self.end_date.timestamp()}"

    @classmethod
    def from_file_format(cls, activity_srt: str):
        data = activity_srt.split(' ')
        if len(data) != 3:
            raise ValueError("data is not formatted correctly")
        name = data[0]
        start_timestamp = datetime.fromtimestamp(float(data[1]))
        end_timestamp = datetime.fromtimestamp(float(data[2]))
        return cls(name, start_timestamp, end_timestamp)

    @property
    def name(self) -> str:
        return self._name

    @property
    def hour(self) -> str:
        return self._hour

    @property
    def start_date(self) -> datetime:
        return self._start_date

    @property
    def end_date(self) -> datetime:
        return self._end_date

    # ensures that the types are good
    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @hour.setter
    def hour(self, new_hour: str):
        self._hour = new_hour

    @start_date.setter
    def start_date(self, new_start_date: datetime):
        self._start_date = new_start_date

    @end_date.setter
    def end_date(self, new_end_date: datetime):
        self._end_date = new_end_date
