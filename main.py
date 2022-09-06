import questionary

import data
import qt
from habit import Habit

print("Hello! This APP aims to improve your efficiency and "
      "let’s you manage and analyze your habits with ease. ")

data.connect_database()


#  CLI Interface
def menu():
    choice = questionary.select(
        "Select one of the following:",
        choices=[
            "Create new Habits",
            "Delete existing Habits",
            "Check off existing Habits",
            "Show Habits (sorted by priority)",
            "Analytics",
            "Exit"
        ]).ask()

    if choice == "Create new Habits":
        habit_name = qt.habit_name()
        habit_periodicity = qt.habit_periodicity()
        habit_priority = qt.habit_priority()
        habit = Habit(habit_name, habit_periodicity, habit_priority)
        habit.add()

    if choice == "Delete existing Habits":
        habit_name = qt.habits_from_conn()
        print(habit_name)
        habit = Habit(habit_name)
        if qt.habit_delete_confirmation(habit_name):
            habit.remove()
        else:
            print("\nHabit not removed!)\n")

    if choice == "Check off existing Habits":
        habit_name = qt.habits_from_conn()
        print(habit_name)
        habit = Habit(habit_name)
        habit.complete()

    if choice == "Show Habits (sorted by priority)":
        pass

    if choice == "Analytics":
        pass

    if choice == "Exit":
        exit()  # exit() completely exits the program


if __name__ == "__main__":
    while True:
        menu()
