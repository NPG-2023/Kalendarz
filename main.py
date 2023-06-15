from tkinter import Tk
from gui import CalendarGUI


def main():
    root = Tk()
    my_gui = CalendarGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

