import sqlite3

from data import conn
from datetime import datetime
import data


class Habit:

#    def __int__(self, name, description, priority, period):
#        self.name = name
#        self.description = description
#        self.priority = priority
#        self.period = period
#        self.startdate = datetime.now()


    def __init__(self, name, description, priority, period):

        self.name = name
        self.description = description
        self.priority = priority
        self.data = sqlite3.connect("test.db")
        self.period = period
        self.startdate = datetime.now().strftime("%m/%d/%Y %H:%M")

    def create_habits(self):

        data.add_habit(self.name, self.description, self.priority, self.period, self.startdate)
        data.update_habits_records(self.name, self.description, self.period, False, 0)
        print("Habit"+self.name+"successfully added!")



