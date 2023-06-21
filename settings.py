import os


class Settings:
    relative_settings_path = "./settings.txt"
    default_calendar_path = "./calendar.txt"

    def __init__(self):
        if os.path.isfile(Settings.relative_settings_path):
            with open(Settings.relative_settings_path, 'r') as file:
                lines = file.readlines()
                if len(lines) > 0:
                    self.calendar_path = lines[0]
                else:
                    self.calendar_path = Settings.default_calendar_path
        else:
            self.calendar_path = Settings.default_calendar_path

    def __del__(self):
        with open(Settings.relative_settings_path, 'w') as file:
            file.write(self.calendar_path)
