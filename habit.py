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
        self.startdate = datetime.now().strftime("%d/%m/%y")
        self.last_completed = None
        self.due = None #self.startdate + datetime.timedelta(days=self.period)
        self.checked = 0
        self.streak = 0
        self.data = sqlite3.connect("test.db")

    def create_habits(self):

        data.add_habit( self.name, self.description, self.priority, self.period, self.startdate)
        data.update_events(self.name, self.description, self.period, self.checked, self.streak,
                                   self.last_completed, self.due)
        print("Habit"+self.name+"successfully added!")

    def remove_habits(self):
        data.remove_habit(self.name)
        data.remove_event(self.name)
        print("Habit" + self.name + "successfully removed!")



