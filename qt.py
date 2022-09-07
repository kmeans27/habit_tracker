import questionary
from data import connect_database, get_habits

def habit_name():
    return questionary.text("Habit Name:").ask().lower()

def habit_periodicity():
    return questionary.select("Habit Periodicity:",
                     choices=["Daily", "Weekly"]).ask().lower()

def habit_priority():
    return questionary.text("Prioritizing your Habits is very important! Here is a short tip to help you with that!\n"
                            "'A' - your most important tasks\n"
                            "'B' - the next most important tasks\n"
                            "'C' - a task you could do but does not have any real consequences if you don't do it\n"
                            "'D' - tasks you can delegate to someone\n"
                            "'E' - tasks that you don't really have to do\n" 
                            "Concept from 'Eat that Frog - Brian Tracy'\n"
                            "\nEnter a character to Prioritize your Habits").ask().lower()


def habits_from_conn():
    conn = connect_database()
    list_of_habits = get_habits(conn)
    return questionary.select("Select a Habit",
                         choices=sorted(list_of_habits)).ask().lower()

def habit_delete_confirmation(habit_name_to_delete):
    return questionary.confirm(f"Do you want to delete the habit: '{habit_name_to_delete}'?").ask()



