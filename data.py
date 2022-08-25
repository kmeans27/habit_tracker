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
        #cursor.execute(f"DELETE FROM habits WHERE name == '{habit_name}'")
        cursor.execute("""DELETE FROM habits WHERE name =?""", (habit_name,))

    #remove_event(habit_name)


def remove_event(habit_name):
    with conn:
        #cursor.execute(f"DELETE FROM events WHERE name == '{habit_name}'")
        cursor.execute("""DELETE FROM events WHERE name =?""", (habit_name,))


def get_habits():
    # cursor.execute("SELECT * FROM habits")
    # print(cursor.fetchall())
    conn.row_factory = lambda cursor, row: row[0]
    result = cursor.execute("SELECT name FROM habits").fetchall()
    return [i[0] for i in result]
    # cursor.execute("SELECT name FROM habits")
    # data = cursor.fetchall()
    # return [i[0] for i in data]



def update_events(name, checked, streak, completed):
    with conn:
        cursor.execute(
            "INSERT INTO events VALUES (?, ?, ?, ?)",
            (name, checked, streak, completed))


def select_habit():
    habits = get_habits()
    return questionary.select("Please Select a Habit",
                     choices=sorted(habits)).ask()


def get_period(habit_name):
    cursor.execute("SELECT period FROM habits WHERE name =?", (habit_name,))
    result = cursor.fetchall()
    return (result[0][0])


def get_completed(habit_name):
    cursor.execute("SELECT completed FROM events WHERE name=?", (habit_name,))
    result = cursor.fetchall()
    return (result[0][0])


def get_streak(habit_name):
    cursor.execute("SELECT streak FROM events WHERE name =?", (habit_name,))
    result = cursor.fetchall()
    return (result[0][0])


def update_streak(habit_name, streak, completed=None):
    with conn:
        cursor.execute("UPDATE events SET streak = ?, completed = ? WHERE habit = ?",
                       (streak, completed, habit_name))

def get_all_data():
    cursor.execute("SELECT * FROM habits")
    result = cursor.fetchall()
    return result




print(get_habits())
# print(get_all_data())
#remove_habit("time")