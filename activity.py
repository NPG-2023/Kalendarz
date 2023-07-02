from datetime import datetime


class Activity:

    def __init__(self, name: str, place: str, date1: datetime, date2: datetime):
        if date1 > date2:
            self._end_date = date1
            self._start_date = date2
        else:
            self._end_date = date2
            self._start_date = date1

        self._name = name
        self._place = place

    def __str__(self) -> str:
        return f"{self.name} miejsce: {self.place} zaczyna się: {self.start_date} i kończy: {self.end_date}"
    # makes the fields readonly

    def to_file_format(self) -> str:
        return f"{self.name} {self.place} {self.start_date.timestamp()} {self.end_date.timestamp()}"

    @classmethod
    def from_file_format(cls, activity_srt: str):
        data = activity_srt.split(' ')
        if len(data) != 4:
            raise ValueError("data is not formatted correctly")
        name = data[0]
        place = data[1]
        start_timestamp = datetime.fromtimestamp(float(data[2]))
        end_timestamp = datetime.fromtimestamp(float(data[3]))
        return cls(name, place, start_timestamp, end_timestamp)

    @property
    def place(self) -> str:
        return self._place

    @property
    def name(self) -> str:
        return self._name

    @property
    def start_date(self) -> datetime:
        return self._start_date

    @property
    def end_date(self) -> datetime:
        return self._end_date

    # ensures that the types are good
    @place.setter
    def place(self, new_place: str):
        self._place = new_place

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @start_date.setter
    def start_date(self, new_start_date: datetime):
        self._start_date = new_start_date

    @end_date.setter
    def end_date(self, new_end_date: datetime):
        self._end_date = new_end_date
