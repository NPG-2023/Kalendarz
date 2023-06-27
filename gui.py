from tkinter import *
from tkcalendar import *
from datetime import datetime
# from tkinter import messagebox
from activity import Activity


class CalendarGUI:
    def __init__(self, master, calendar):
        self.master = master
        self.my_label = Label(self.master, text=f"Selected Date: ")
        self.master.geometry("600x600")
        self.calendar = calendar
        self.cal = Calendar(self.master, selectmode="day", locale="pl_PL")
        self.cal.pack(pady=10, fill="both", expand=True)

        self.add_button = Button(self.master, text="Dodaj Wydarzenie", command=self.add_event)
        self.add_button.pack(pady=0)

        self.event_info_label = Label(self.master, text="")
        self.event_info_label.pack(pady=10)

        self.input_frame = None
        self.activity_list = None
        self.data = {}
        self.event_start_date_entry = None
        self.event_end_date_entry = None
        self.event_start_hour_entry = None
        self.event_end_hour_entry = None
        self.event_name_entry = None

        self.cal.bind("<<CalendarSelected>>", self.show_events)

    def show_events(self, *args):
        date = self.cal.get_date()
        year = int(date.split('.')[2])
        month = int(date.split('.')[1])
        day = int(date.split('.')[0])

        activities = self.calendar.get_activities_from_range(
            datetime(year, month, day, 0, 0),
            datetime(year, month, day, 23, 59),
            only_inclusion=False
        )
        if self.activity_list is not None:
            self.activity_list.destroy()
            self.activity_list = None

        if len(activities) == 0:
            self.event_info_label.config(text="W tym dniu nie ma wydarzeń")
            return

        self.event_info_label.config(text="")
        activity_list = Frame()
        activity_list.pack()
        self.activity_list = activity_list

        for i, act in enumerate(activities):
            text = Label(activity_list, text=str(act))
            text.grid(row=i, column=0)

            def on_del():
                self.calendar.remove_activity(act)
                self.show_events()

            del_button = Button(
                activity_list,
                command=on_del,
                text="Usuń"
            )
            del_button.grid(row=i, column=1)

            edit_button = Button(
                activity_list,
                command=lambda: self.edit_event(act),
                text="Edytuj"
            )
            edit_button.grid(row=i, column=2)

    def render_input_frame(self):
        if self.input_frame is not None:
            self.input_frame.destroy()

        self.my_label.config(text="" + self.cal.get_date())

        input_frame = Frame(self.master, width=450, height=200, pady=3)

        self.input_frame = input_frame
        input_frame.pack()

        event_start_date_label = Label(input_frame, text="Data startu:")
        event_start_date_label.grid(row=0, column=0)

        event_start_date_entry = DateEntry(input_frame, width=50, locale="pl_PL")
        event_start_date_entry.grid(row=1, column=0)
        event_start_date_entry.set_date(self.cal.get_date())
        self.event_start_date_entry = event_start_date_entry

        event_start_hour_label = Label(input_frame, text="Godzina startu:")
        event_start_hour_label.grid(row=0, column=1)

        event_start_hour_entry = Entry(input_frame)
        event_start_hour_entry.grid(row=1, column=1)
        self.event_start_hour_entry = event_start_hour_entry

        event_end_date_label = Label(input_frame, text="Data końca:")
        event_end_date_label.grid(row=2, column=0)

        event_end_date_entry = DateEntry(input_frame, width=50, locale="pl_PL")
        event_end_date_entry.grid(row=3, column=0)
        event_end_date_entry.set_date(self.cal.get_date())
        self.event_end_date_entry = event_end_date_entry

        event_end_hour_label = Label(input_frame, text="Godzina końca:")
        event_end_hour_label.grid(row=2, column=1)

        event_end_hour_entry = Entry(input_frame)
        event_end_hour_entry.grid(row=3, column=1)
        self.event_end_hour_entry = event_end_hour_entry

        event_name_label = Label(input_frame, text="Nazwa:")
        event_name_label.grid(row=4, column=0, columnspan=2)

        event_name_entry = Entry(input_frame, width=50)
        event_name_entry.grid(row=5, column=0, columnspan=2)
        self.event_name_entry = event_name_entry

    def add_event(self):
        self.render_input_frame()
        save_button = Button(self.input_frame, text="Dodaj", command=self.save_event)
        save_button.grid(row=6, column=0, columnspan=2)

    def save_event(self, act=None):
        start_date = self.event_start_date_entry.get()
        start_hour = self.event_start_hour_entry.get()
        end_date = self.event_end_date_entry.get()
        end_hour = self.event_end_hour_entry.get()
        name = self.event_name_entry.get()

        if start_hour == "" or end_hour == "":
            self.event_info_label.config(text="Podaj obie godziny!")
            return

        start_datetime = datetime(
            int(start_date.split('.')[2]),
            int(start_date.split('.')[1]),
            int(start_date.split('.')[0]),
            int(start_hour.split(':')[0]),
            int(start_hour.split(':')[1]))

        end_datetime = datetime(
            int(end_date.split('.')[2]),
            int(end_date.split('.')[1]),
            int(end_date.split('.')[0]),
            int(end_hour.split(':')[0]),
            int(end_hour.split(':')[1]))

        if act is None:
            self.calendar.add_activity(Activity(name, start_datetime, end_datetime))
        else:
            self.calendar.change_activity_dates(act, start_datetime, end_datetime)
            self.calendar.change_activity_name(act, name)

        self.input_frame.destroy()
        self.input_frame = None

    def edit_event(self, activity_to_edit):
        self.render_input_frame()
        if self.activity_list is not None:
            self.activity_list.destroy()
            self.activity_list = None

        self.event_info_label.config(text="Edytujesz: " + str(activity_to_edit))

        self.event_start_date_entry.set_date(activity_to_edit.start_date)
        self.event_end_date_entry.set_date(activity_to_edit.end_date)
        self.event_start_hour_entry.insert(
            0,
            format(activity_to_edit.start_date.hour, '02') + ":" + format(activity_to_edit.start_date.minute, '02'))

        self.event_end_hour_entry.insert(
            0,
            format(activity_to_edit.end_date.hour, '02') + ":" + format(activity_to_edit.end_date.minute, '02'))
        self.event_name_entry.insert(0, activity_to_edit.name)

        save_button = Button(self.input_frame, text="Zapisz Zmiany", command=lambda: self.save_event(activity_to_edit))
        save_button.grid(row=6, column=0, columnspan=2)
