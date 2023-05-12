from tkinter import *
from tkcalendar import *
from tkinter import messagebox


class CalendarGUI:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x600")

        self.cal = Calendar(self.master, selectmode="day", year=2023, month=4, day=16)
        self.cal.pack(pady=10, fill="both", expand=True)

        self.my_button = Button(self.master, text="Dodaj Wydarzenie", command=self.grab_date)
        self.my_button.pack(pady=0)

        self.my_label = Label(self.master, text="")
        self.my_label.pack(pady=20)

    def grab_date(self):
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

        messagebox.showinfo(title="Wydarzenie zapisane",
                            message=f"Zapisano wydarzenie: '{event_desc}' w dniu {event_date} o godzinie {event_hour}")

        self.event_desc_entry.delete(0, END)
        self.event_hour_entry.delete(0, END)


