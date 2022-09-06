from data import connect_database


def habit_due():
    conn = connect_database()
    cursor = conn.cursor()
    result = cursor.execute("SELECT name FROM habits WHERE streak = 0").fetchall()
    print(result)

def currently_tracked():
    conn = connect_database()
    cursor = conn.cursor()
    result = cursor.execute("SELECT name FROM habits").fetchall()
    print(result)

def same_periodcitiy(periodicity):
    conn = connect_database()
    cursor = conn.cursor()
    query = "SELECT name FROM habits WHERE periodicity = ?"
    result = cursor.execute(query, (periodicity,)).fetchall()
    print(result)

def longest_streak():
    conn = connect_database()
    cursor = conn.cursor()
    result = cursor.execute("SELECT name, MAX(streak) FROM events").fetchall()
    print(result)

def given_habit_longest_streak(habit_name):
    conn = connect_database()
    cursor = conn.cursor()
    query = "SELECT name, MAX(streak) FROM events WHERE name = ?"
    result = cursor.execute(query, (habit_name,)).fetchall()
    print(result)
