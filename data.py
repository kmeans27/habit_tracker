import datetime
import sqlite3
from datetime import datetime

import questionary

conn = sqlite3.connect("test3.db")
cursor = conn.cursor()

def create_table():
    with conn:
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS habits (
                    name text PRIMARY KEY,
                    description text,
                    priority char,
                    period int,
                    startdate text )
            """)

    with conn:
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS habits_records (
                    name text,
                    description text,
                    period int,
                    checked boolean DEFAULT False,
                    streak int DEFAULT 0,
                    due text,
                    last_completed text,
                    FOREIGN KEY (name) REFERENCES habits(name)
                    FOREIGN KEY (description) REFERENCES habits(description)
                    FOREIGN KEY (period) REFERENCES habits(period) )
            """)

create_table()
def add_habit(name, description, priority, period, startdate):
    with conn:
        cursor.execute(
            "INSERT INTO habits VALUES (?, ?, ?, ?, ?)",
            (name, description, priority, period, startdate))


def remove_habit(habit_name):
    with conn:
        cursor.execute(f"DELETE FROM habits WHERE name == '{habit_name}'; ")

# def get_habits():
#     with conn:
#          cursor.execute("SELECT name FROM habits")
#          habit_names = cursor.fetchall()
#          return habit_names

def get_habits():
    with conn:
         cursor.execute("SELECT name FROM habits")
         habit_names = cursor.fetchall()
         return [i[0] for i in set(habit_names)]


def update_habits_records(name, description, period, last_completed, due, checked, streak):
    with conn:
         cursor.execute(
             "INSERT INTO habits_records VALUES (?, ?, ?, ?, ?, ?, ?)",
              (name, description, period, last_completed, due, checked, streak))

def select_habit():
    habits_list = get_habits()
    if habits_list is not None:
        return questionary.select("Select a habit:",
                                  choices=sorted(habits_list)).ask().lower()
    else:
        raise ValueError("No habits found")

# def get_checked_and_due():
#     with conn:
#         cursor.execute("SELECT checked, due FROM habits_records")
#         checked_due_data = cursor.fetchall()
#         return [i[0] for i in set(checked_due_data)]

def complete_functionality(habit_name):
    last_completed = datetime.now()
    due = datetime.now() + datetime.timedelta(days=2)
    name = habit_name
    with conn:
    #     cursor.execute("SELECT name, period FROM habits WHERE name = ?", name = habit_name)
    #     data = cursor.fetchall()
    #     print(data)

        cursor.execute("UPDATE habits_records SET last_completed = ?, due = ?, checked = FALSE "
                       "WHERE name = ?",
                       (last_completed, due, name))







