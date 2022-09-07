import datetime
import sqlite3
from datetime import datetime
import questionary


def connect_database(name="new.db"):
    """
    Creates a database connection using sqlite3
    :param name: Name of the .db file
    :return: Returns the connection
    """
    conn = sqlite3.connect(name)
    create_tables(conn)
    return conn

def create_tables(conn):
    """
    Creates following tables: habits, events
    :param conn: Connect with the database file
    :return:
    """
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
    """
    Adds a habit to the habits table
    :param conn: Connect with the database file
    :param name: Name of the habit
    :param periodicity: Periodicity of the habit. Either daily or weekly
    :param priority: Priority of the habit. A, B, C, D, or E is suggested
    :param creation_time: The time the habit was created
    :param streak: How often the habit is completed within the defined period. Default 0
    :param completion_time: The time the habit was lastly marked as completed
    :return:
    """
    cursor = conn.cursor()
    cursor.execute("INSERT INTO habits VALUES(?, ?, ?, ?, ?, ?)",
                    (name, periodicity, priority,
                    creation_time, streak, completion_time))
    conn.commit()


def remove_habit(conn, habit_name):
    """
    Removes a habit from the "habits" table. "Remove_events" also removes the habit on the "events" table.
    :param conn: Connect with database file
    :param habit_name: Name of the habit that should be deleted
    :return:
    """
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM habits WHERE name =?""", (habit_name,))
    conn.commit()
    remove_events(conn, habit_name)

def remove_events(conn, habit_name):
    """
    Removes the habit from the "events" table.
    :param conn: Connect with database file
    :param habit_name: Name of the habit that should be deleted
    :return:
    """
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM events WHERE name =?""", (habit_name,))
    conn.commit()


def get_habits(conn):
    """
    Returns the name of all habits within the table "habits"
    :param conn: Connect with database file
    :return: name of all habits in "habits" table
    """
    cursor = conn.cursor()
    result = cursor.execute("SELECT name FROM habits").fetchall()
    return [i[0] for i in result]


def update_events(conn, name, is_completed, streak, completion_time):
    """
    Updates the "events" table
    :param conn: Connect with database file
    :param name: Name of the habit that should be updated
    :param is_completed: Gets if the habit is already completed or not
    :param streak: Streak of a habit
    :param completion_time: Time of completion
    :return:
    """
    cursor = conn.cursor()
    cursor.execute("INSERT INTO events VALUES(?, ?, ?, ?)",
                    (name, is_completed, streak, completion_time))
    conn.commit()


def get_period(conn, habit_name):
    """
    Gets the periodicity of a certain habit
    :param conn: Connect with database file
    :param habit_name: Name of the habit
    :return: returns the periodicity
    """
    cursor = conn.cursor()
    query = "SELECT periodicity FROM habits WHERE name =?"
    cursor.execute(query, (habit_name,))
    data = cursor.fetchall()
    return data[0][0]


def get_habit_completion_time(conn, habit_name):
    """
    Gets the completion time of a certain habit
    :param conn: Connect with database file
    :param habit_name: Name of the habit
    :return: returns the completion time
    """
    cursor = conn.cursor()
    query = "SELECT completion_time FROM habits WHERE name = ?"
    cursor.execute(query, (habit_name,))
    data = cursor.fetchall()
    return data[0][0]


def get_streak_count(conn, habit_name):
    """
    Gets the streak count of a certain habit
    :param conn: Connect with database file
    :param habit_name: Name of the habit
    :return: returns the streak count
    """
    cursor = conn.cursor()
    query = "SELECT streak FROM habits WHERE name = ?"
    cursor.execute(query, (habit_name,))
    streak_count = cursor.fetchall()
    return streak_count[0][0]


def update_habit_streak(conn, habit_name, streak, time=None):
    """
    Updates a habit ´s streak
    :param conn: Connect with database file
    :param habit_name: Name of the habit that should be updated
    :param streak: Streak of the habit. How often it has been completed within the defined periodicity
    :param time: Time when the habit has been updated
    :return:
    """
    cursor = conn.cursor()
    query = "UPDATE habits SET streak = ?, completion_time = ? WHERE name = ?"
    data = (streak, time, habit_name)
    cursor.execute(query, data)
    conn.commit()


def get_all_data(conn):
    """
    Returns all data from the "habits" table. Testing purposes
    :param conn: Connect with database file
    :return: returns all data
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM habits")
    result = cursor.fetchall()
    return result


def fetch_priority(conn):
    """
    Gets all the different priorities within the "habits" table
    :param conn: Connect with database file
    :return: returns the priority characters
    """
    cursor = conn.cursor()
    cursor.execute("SELECT priority FROM habits")
    data = cursor.fetchall()
    return [i[0] for i in set(data)]

