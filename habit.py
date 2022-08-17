import sqlite3
import itertools
from data import conn
import datetime
from datetime import datetime

import data


class Habit:

    def __init__(self, name, description, priority, period ):
        self.name = name
        self.description = description
        self.priority = priority
        self.period = period
        self.startdate = datetime.now().strftime("%d/%m/%y %H:%M")
        self.completed = None
        self.checked = 0
        self.streak = 0

    def create_habits(self):
        data.add_habit(self.name, self.description, self.priority, self.period, self.startdate)
        data.update_events(self.name, self.checked, self.streak, self.completed)
        print("Habit"+self.name+"successfully added!")

    def remove_habits(self):
        data.remove_habit(self.name)
        data.remove_event(self.name)
        print("Habit" + self.name + "successfully removed!")

    def daily_streak(self):
        complete = data.get_completed(self.name)
        streak = data.get_streak(self.name)
        if streak == 0 or complete is None:
            return 1
        else:
            date = datetime.strptime(self.startdate[:10], "%d/%m/%y") - datetime.strptime(complete[:10], "%d/%m/%y")
            return date.days

    def increment_streak(self):
        self.streak = data.get_streak(self.name)
        self.streak += 1

    def update_streak(self):
        self.increment_streak()
        data.update_streak(self.name, self.streak, self.completed())
        data.update_events(self.name, True, data.get_streak(self.name), self.completed())
        print(f"\nUpdated streak for: '{self.name}' is '{self.streak}'")

    def reset_streak(self):
        self.streak = 1
        data.update_streak(self.name, self.streak, self.completed())
        data.update_events(self.name, True, data.get_streak(self.name), self.completed())
        print(f"\nStreak for habit: '{self.name}' is reset: '{self.streak}'")

    def completed(self):
        if data.get_period(self.name) == "daily":
            if self.daily_streak() == 0:
                print("\nAlready completed today!")
            elif self.daily_streak() == 1:
                self.update_streak()
            else:
                self.reset_streak()





