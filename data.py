import sqlite3
from datetime import date

conn = sqlite3.connect("test.db")
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
                    checked boolean,
                    streak int DEFAULT 0,
                    FOREIGN KEY (name) REFERENCES habits(name)
                    FOREIGN KEY (description) REFERENCES habits(description)
                    FOREIGN KEY (period) REFERENCES habits(period) )
            """)


def add_habit(name, description, priority, period, startdate):
    with conn:
        cursor.execute(
            "INSERT INTO habits VALUES (?, ?, ?, ?, ?)",
            (name, description, priority, period, startdate))


def remove_habit(habit_name):
    with conn:
        cursor.execute(f"DELETE FROM habits WHERE name == '{habit_name}'; ")


def update_habits_records(name, description, period, checked, streak):
    with conn:
         cursor.execute(
             "INSERT INTO habits_records VALUES (?, ?, ?, ?, ?)",
              (name, description, period, checked, streak))





