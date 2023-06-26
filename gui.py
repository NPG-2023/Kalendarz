from tkinter import *
from tkcalendar import *
# from tkinter import messagebox
# from activity import Activity


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

        self.check_button = Button(self.master, text="Sprawdz wydarzenie", command=self.pick_date)
        self.check_button.pack(pady=0)

        self.edit_button = Button(self.master, text="Edytuj wydarzenie", command=self.edit_activity)
        self.edit_button.pack(pady=0)

        self.event_info_label = Label(self.master, text="")
        self.event_info_label.pack(pady=10)

        self.to_del = []
        self.data = {}

    def edit_activity(self):
        pass
        # selected_date = self.cal.get_date()
        # activities = self.calendar.get_activities_from_range(selected_date, selected_date, only_inclusion=True)
        # if activities:
        #     # zmien nazwe i date wydarzeni
        #     self.grab_date(command="edycja")
        # else:
        #     event_info = "Brak wydarzeń do edycji."
        #     self.event_info_label.config(text=event_info)

    def pick_date(self):
        selected_date = self.cal.get_date()
        activities = self.calendar.get_activities_from_range(selected_date, selected_date, only_inclusion=True)
        if activities:
            event_info = "\n".join(str(activity) for activity in activities)
        else:
            event_info = "Brak wydarzeń dla tej daty."
        self.event_info_label.config(text=event_info)

    def add_event(self, command= ""):
        self.my_label.config(text="" + self.cal.get_date())

        input_frame = Frame(self.master, width=450, height=200, pady=3)

        self.to_del.append(input_frame)
        input_frame.pack()

        event_start_date_label = Label(input_frame, text="Data startu:")
        event_start_date_label.grid(row=0, column=0)

        event_start_date_entry = DateEntry(input_frame, width=50)
        event_start_date_entry.grid(row=1, column=0)

        event_start_hour_label = Label(input_frame, text="Godzina startu:")
        event_start_hour_label.grid(row=0, column=1)

        event_start_hour_entry = Entry(input_frame)
        event_start_hour_entry.grid(row=1, column=1)

        event_end_date_label = Label(input_frame, text="Data końca:")
        event_end_date_label.grid(row=2, column=0)

        event_end_date_entry = DateEntry(input_frame, width=50)
        event_end_date_entry.grid(row=3, column=0)

        event_end_hour_label = Label(input_frame, text="Godzina końca:")
        event_end_hour_label.grid(row=2, column=1)

        event_end_hour_entry = Entry(input_frame)
        event_end_hour_entry.grid(row=3, column=1)

        # wprowadzenie nazwy wydarzenia
        event_name_label = Label(input_frame, text="Nazwa:")
        event_name_label.grid(row=4, column=0, columnspan=2)

        event_name_entry = Entry(input_frame, width=50)
        event_name_entry.grid(row=5, column=0, columnspan=2)

        save_button = Button(input_frame, text="Zapisz", command=self.save_event)
        save_button.grid(row=6, column=0, columnspan=2)

    def save_event(self):
        for w in self.to_del:
            w.destroy()
        # event_date = self.cal.get_date()  # dodaj wydarzenie
        # event_desc = self.event_desc_entry.get()
        # event_hour = self.event_hour_entry.get()
        #
        # event_info = f"Zapisano wydarzenie: '{event_desc}' w dniu {event_date} o godzinie {event_hour}"
        # self.event_info_label.config(text=event_info)
        #
        # self.event_desc_entry.delete(0, END)
        # self.event_hour_entry.delete(0, END)
        #
        # self.calendar.add_activity(activity=Activity(event_desc, event_date, event_date, event_hour))

    def edit_event(self, activity_to_edit):
        pass
        # self.calendar.change_activity_name(activity_to_edit, self.event_desc_entry)
        # self.calendar.change_activity_dates(activity_to_edit, self.event_hour_entry)
        #
        # event_info = f"Zapisano wydarzenie: '{self.event_hour_entry}' w dniu {self.event_desc_entry}"
        # self.event_info_label.config(text=event_info)



