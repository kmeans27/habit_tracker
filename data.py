import datetime
import sqlite3
from datetime import datetime


import questionary

conn = sqlite3.connect("test6.db")
cursor = conn.cursor()

def create_table():
    with conn:
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS habits (
                    name text,
                    description text,
                    priority char,
                    period text,
                    startdate text )
            """)

    with conn:
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS events (
                    name text,
                    checked boolean DEFAULT False,
                    streak int DEFAULT 0,
                    completed text,
                    FOREIGN KEY (name) REFERENCES habits(name) )
            """)

create_table()
def add_habit(name, description, priority, period, startdate):
    with conn:
        cursor.execute(
            "INSERT INTO habits VALUES (?, ?, ?, ?, ?)",
            (name, description, priority, period, startdate))


def remove_habit(habit_name):
    with conn:
        cursor.execute(f"DELETE FROM habits WHERE name = '{habit_name}'; ")


def remove_event(habit_name):
    with conn:
        cursor.execute(f"DELETE FROM events WHERE name = '{habit_name}';")


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


def update_events(name, checked, streak, completed):
    with conn:
         cursor.execute(
             "INSERT INTO events VALUES (?, ?, ?, ?)",
              (name, checked, streak, completed))

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

# def complete_functionality(habit_name):
    # with conn:
        # cursor.execute(f"SELECT description FROM events WHERE name == '{habit_name}'")
        # description = cursor.fetchone()
        # cursor.execute("INSERT INTO events VALUES (?, ?, ?, ?, ?, ?, ?)",
        #                (habit_name, description, period, True, 1, None, datetime.now().strftime("%d/%m/%y")))







