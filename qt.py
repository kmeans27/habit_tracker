import questionary
from data import connect_database, fetch_priority, get_habits

def habit_name():
    return questionary.text("Habit Name:").ask().lower()

def habit_periodicity():
    return questionary.select("Habit Periodicity:",
                     choices=["Daily", "Weekly"]).ask().lower()

def habit_priority():
    return questionary.text("Enter a character to Prioritize your Habits").ask().lower()

def defined_priority():
    data = connect_database()
    arr = fetch_priority(data)
    return questionary.select("Select a priority",
                       choices=sorted(arr)).ask().lower()

def priority_delete_confirmation():
    return questionary.confirm("Are you sure?").ask()

def periodicity_change_confirmed():
    return questionary.confirm("Are you sure?").ask()

def habits_from_conn():
    conn = connect_database()
    list_of_habits = get_habits(conn)
    return questionary.select("Select a Habit",
                         choices=sorted(list_of_habits)).ask().lower()

def habit_delete_confirmation(habit_name_to_delete):
    return questionary.confirm(f"Do you want to delete the habit: '{habit_name_to_delete}'?").ask()

def show_period_choices():
    choice = questionary.select("Would you like to view all habits or sort habit by periodicity?",
                       choices=[
                           "View All Habits",
                           "View Daily Habits",
                           "View Weekly Habits",
                           "Back to Menu"
                       ]).ask()
    return choice



