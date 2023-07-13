from tkinter import Tk
from gui import CalendarGUI
from settings import Settings
from ourCalendar import Calendar


def main():
    settings = Settings()
    calendar = Calendar(settings.calendar_path)
    root = Tk()
    root.title("Kalendarz")
    my_gui = CalendarGUI(root, calendar, settings)
    root.mainloop()


if __name__ == "__main__":
    main()

