import sqlite3

from data import conn
from datetime import datetime
import data


class Habit:


    def __init__(self, name, description, priority, period ):

        self.name = name
        self.description = description
        self.priority = priority
        self.period = period
        self.startdate = datetime.now()
        self.data = sqlite3.connect("test.db")

    def create_habits(self):

        data.add_habit(self.name, self.description, self.priority, self.period, self.startdate)
        data.update_habits_records(self.name, self.description, self.period, False, 0)
        print("Habit"+self.name+"successfully added!")



