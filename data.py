import datetime
import sqlite3
from datetime import datetime
import questionary


def connect_database(name="new.db"):
    conn = sqlite3.connect(name)
    create_tables(conn)
    return conn

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS habits (
               name TEXT PRIMARY KEY , 
               periodicity TEXT,
               priority TEXT,
               creation_time TEXT,
               streak INT,
               completion_time TEXT   
           )""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            name TEXT,
            completed Boolean,
            streak INT DEFAULT 0,
            completion_time TIME,
            FOREIGN KEY (name) REFERENCES habits(name)
        )""")
    conn.commit()


def add_habit(conn, name, periodicity, priority, creation_time, streak, completion_time=None):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO habits VALUES(?, ?, ?, ?, ?, ?)",
                    (name, periodicity, priority,
                    creation_time, streak, completion_time))
    conn.commit()


def remove_habit(conn, habit_name):
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM habits WHERE name =?""", (habit_name,))
    conn.commit()
    remove_events(conn, habit_name)

def remove_events(conn, habit_name):
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM events WHERE name =?""", (habit_name,))
    conn.commit()


def get_habits(conn):
    cursor = conn.cursor()
    result = cursor.execute("SELECT name FROM habits").fetchall()
    return [i[0] for i in result]


def update_events(conn, name, is_completed, streak, completion_time):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO events VALUES(?, ?, ?, ?)",
                    (name, is_completed, streak, completion_time))
    conn.commit()


def get_period(conn, habit_name):
    cursor = conn.cursor()
    query = "SELECT periodicity FROM habits WHERE name =?"
    cursor.execute(query, (habit_name,))
    data = cursor.fetchall()
    return data[0][0]


def get_habit_completion_time(conn, habit_name):
    cursor = conn.cursor()
    query = "SELECT completion_time FROM habits WHERE name = ?"
    cursor.execute(query, (habit_name,))
    data = cursor.fetchall()
    return data[0][0]


def get_streak_count(conn, habit_name):
    cursor = conn.cursor()
    query = "SELECT streak FROM habits WHERE name = ?"
    cursor.execute(query, (habit_name,))
    streak_count = cursor.fetchall()
    return streak_count[0][0]


def update_habit_streak(conn, habit_name, streak, time=None):
    cursor = conn.cursor()
    query = "UPDATE habits SET streak = ?, completion_time = ? WHERE name = ?"
    data = (streak, time, habit_name)
    cursor.execute(query, data)
    conn.commit()


def get_all_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM habits")
    result = cursor.fetchall()
    return result


def fetch_priority(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT priority FROM habits")
    data = cursor.fetchall()
    return [i[0] for i in set(data)]

