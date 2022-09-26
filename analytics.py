from data import connect_database
import re

def habit_due():
    """
    Prints the name of all due habits
    :return:
    """
    conn = connect_database()
    cursor = conn.cursor()
    result = cursor.execute("SELECT name FROM habits WHERE streak = 0").fetchall()
    for data in result:
        print(data[0])
    print("\n")

def currently_tracked():
    """
    Prints all habit names
    :return:
    """
    conn = connect_database()
    cursor = conn.cursor()
    result = cursor.execute("SELECT name FROM habits").fetchall()
    # print("\nHabit-names")
    for data in result:
        print(data[0])
    print("\n")

def same_periodcitiy(periodicity):
    """
    Prints all habits with the same periodicty
    :param periodicity: Periodicity of a habit. Either daily or weekly
    :return:
    """
    conn = connect_database()
    cursor = conn.cursor()
    query = "SELECT name FROM habits WHERE periodicity = ?"
    result = cursor.execute(query, (periodicity,)).fetchall()
    for data in result:
        print(data[0])
    print("\n")

def longest_streak():
    """
    Prints the longest streak of any habit
    :return:
    """
    conn = connect_database()
    cursor = conn.cursor()
    result = cursor.execute("SELECT name, MAX(streak) FROM events").fetchall()
    for data in result:
        print(data[0])
    print("\n")

def given_habit_longest_streak(habit_name):
    """
    Prints the longest streak of a given habit
    :param habit_name:
    :return:
    """
    conn = connect_database()
    cursor = conn.cursor()
    query = "SELECT name, MAX(streak) FROM events WHERE name = ?"
    result = cursor.execute(query, (habit_name,)).fetchall()
    print("\n{:10} {:50}".format("Habit-name", "Streak"))
    print(result[0][0], result[0][1])
    print("\n")

def sort_priority():
    """
    Sorts all habit names by priority ascending
    :return:
    """
    conn = connect_database()
    cursor = conn.cursor()
    result = cursor.execute("SELECT name, priority FROM habits ORDER BY priority ASC").fetchall()
    print("\n{:10} {:50}".format("Habit-names", "Priority"))
    for data in result:
        print("{:10} {:50}".format(data[0], data[1]))
    print("\n")
