from tkinter import Tk
from gui import CalendarGUI
from settings import Settings
from ourCalendar import Calendar


def main():
    settings = Settings()
    calendar = Calendar(settings.calendar_path)
    root = Tk()
    my_gui = CalendarGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

