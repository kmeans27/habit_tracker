import questionary
import analytics
import data
import qt
from habit import Habit

print("Hello! This APP aims to improve your efficiency and "
      "let’s you manage and analyze your habits with ease. ")

data.connect_database()


#  CLI Interface
def menu():
    """
    Used to maintain a loop so the user can do more than one action before the app closes itself.
    :return:
    """
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
        print("\nYour currently tracked Habits sorted by priority:\n")
        analytics.sort_priority()

    if choice == "Analytics":
        second_choice = questionary.select(
            "Choose one of the following",
            choices=[
                "View due Habits",
                "View all currently tracked Habits",
                "View all Habits with same periodicity",
                "View Longest Streak",
                "View Longest Streak of a given Habit"
            ]).ask()

        if second_choice == "View due Habits":
            print("\nThe following Habits are currently due:\n")
            analytics.habit_due()

        if second_choice == "View all currently tracked Habits":
            print("\nThe following Habits are currently tracked:\n")
            analytics.currently_tracked()

        if second_choice == "View all Habits with same periodicity":
            print("\nPlease enter either 'Daily' or 'Weekly' (Weekly is currently not supported)\n")
            periodicity = questionary.text("Periodicity:").ask().lower()
            print(periodicity)
            print("\nThe Habits with the same periodicity are:\n")
            analytics.same_periodcitiy(periodicity)

        if second_choice == "View Longest Streak":
            print("\nThe Habit with the longest run streak is:\n")
            analytics.longest_streak()

        if second_choice == "View Longest Streak of a given Habit":
            print("\nSelect one of the following Habits:\n")
            habit_name = qt.habits_from_conn()
            print(f"You selected the Habit: '{habit_name}'")
            analytics.given_habit_longest_streak(habit_name)


    if choice == "Exit":
        exit()  # exit() completely exits the program


if __name__ == "__main__":
    while True:
        menu()
