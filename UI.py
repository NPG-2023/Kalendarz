import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

class EventCalendar:
    def __init__(self, master):
        self.master = master
        self.master.title("Event Calendar")

        self.calendar = ttk.Calendar(self.master, selectmode="day")
        self.calendar.pack(pady=10)

        self.event_label = ttk.Label(self.master, text="Event:")
        self.event_label.pack()

        self.event_entry = ttk.Entry(self.master)
        self.event_entry.pack()

        self.add_button = ttk.Button(self.master, text="Add", command=self.add_event)
        self.add_button.pack(pady=10)

    def add_event(self):
        selected_date = self.calendar.selection()
        event_text = self.event_entry.get()
        if selected_date:
            event_date = selected_date[0]
            event_date_str = event_date.strftime("%Y-%m-%d")
            messagebox.showinfo("Event Added", f"Added event '{event_text}' on {event_date_str}")
        else:
            messagebox.showerror("Error", "No date selected")

root = tk.Tk()
event_calendar = EventCalendar(root)
root.mainloop()
