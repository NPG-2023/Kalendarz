from tkinter import *
from tkcalendar import *
from tkinter import messagebox
from activity import Activity

class CalendarGUI:
    def __init__(self, master, calendar):
        self.master = master
        self.my_label = Label(self.master, text=f"Selected Date: ")
        self.master.geometry("600x600")
        self.calendar = calendar
        self.cal = Calendar(self.master, selectmode="day", year=2023, month=4, day=16)
        self.cal.pack(pady=10, fill="both", expand=True)

        self.my_button = Button(self.master, text="Dodaj Wydarzenie", command=self.grab_date)
        self.my_button.pack(pady=0)

        self.my_button = Button(self.master, text="Sprawdz wydarzenie", command=self.pick_date)
        self.my_button.pack(pady=0)

        self.my_button = Button(self.master, text="Edytuj wydarzenie", command=self.edit_activity)
        self.my_button.pack(pady=0)

        self.event_info_label = Label(self.master, text="")
        self.event_info_label.pack(pady=10)

    def edit_activity(self):
        selected_date = self.cal.get_date()
        activities = self.calendar.get_activities_from_range(selected_date, selected_date, only_inclusion=True)
        if activities:
            # zmien nazwe i date wydarzeni
            self.grab_date(command="edycja")
        else:
            event_info = "Brak wydarzeń do edycji."
            self.event_info_label.config(text=event_info)

    def pick_date(self):
        selected_date = self.cal.get_date()
        activities = self.calendar.get_activities_from_range(selected_date, selected_date, only_inclusion=True)
        if activities:
            event_info = "\n".join(str(activity) for activity in activities)
        else:
            event_info = "Brak wydarzeń dla tej daty."
        self.event_info_label.config(text=event_info)

    def grab_date(self, command= ""):
        if command == "":
            command = self.save_event
        if command == "edycja":
            command = self.edit_event(self.calendar.get_activities_from_range(self.cal.get_date(), self.cal.get_date(), only_inclusion=True)[0])
        command = command
        self.my_label.config(text="" + self.cal.get_date())

        # wprowadzenie godziny wydarzenia
        event_hour_label = Label(self.master, text="Godzina wydarzenia:")
        event_hour_label.pack(pady=10)

        self.event_hour_entry = Entry(self.master, width=50)
        self.event_hour_entry.pack()

        # wprowadzenie opisu wydarzenia
        event_desc_label = Label(self.master, text="Opis wydarzenia:")
        event_desc_label.pack(pady=10)
        self.event_desc_entry = Entry(self.master, width=50)
        self.event_desc_entry.pack()

        self.save_button = Button(self.master, text="Zapisz", command=self.save_event)
        self.save_button.pack(pady=10)

    def save_event(self):
        event_date = self.cal.get_date()  # dodaj wydarzenie
        event_desc = self.event_desc_entry.get()
        event_hour = self.event_hour_entry.get()

        event_info = f"Zapisano wydarzenie: '{event_desc}' w dniu {event_date} o godzinie {event_hour}"
        self.event_info_label.config(text=event_info)

        self.event_desc_entry.delete(0, END)
        self.event_hour_entry.delete(0, END)

        self.calendar.add_activity(activity=Activity(event_desc, event_date, event_date, event_hour))




    def edit_event(self, activityToEdit):

        self.calendar.change_activity_name(activityToEdit, self.event_desc_entry)
        self.calendar.change_activity_dates(activityToEdit, self.event_hour_entry)

        event_info = f"Zapisano wydarzenie: '{self.event_hour_entry}' w dniu {self.event_desc_entry}"
        self.event_info_label.config(text=event_info)



