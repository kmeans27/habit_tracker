from data import connect_database


def habit_due():
    """
    Prints the name of all due habits
    :return:
    """
    conn = connect_database()
    cursor = conn.cursor()
    result = cursor.execute("SELECT name FROM habits WHERE streak = 0").fetchall()
    print(result)

def currently_tracked():
    """
    Prints all habit names
    :return:
    """
    conn = connect_database()
    cursor = conn.cursor()
    result = cursor.execute("SELECT name FROM habits").fetchall()
    print(result)

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
    print(result)

def longest_streak():
    """
    Prints the longest streak of any habit
    :return:
    """
    conn = connect_database()
    cursor = conn.cursor()
    result = cursor.execute("SELECT name, MAX(streak) FROM events").fetchall()
    print(result)

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
    print(result)

def sort_priority():
    """
    Sorts all habit names by priority ascending
    :return:
    """
    conn = connect_database()
    cursor = conn.cursor()
    result = cursor.execute("SELECT name, priority FROM habits ORDER BY priority ASC").fetchall()
    print(result)