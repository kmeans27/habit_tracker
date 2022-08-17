import data
from habit import Habit

import questionary
from datetime import datetime

print("Hello! This APP aims to improve your efficiency and "
      "let’s you manage and analyze your habits with ease. ")

if __name__ == '__main__':
    # molsou = Habit("justtest", "this is the description", "B", 2)
    # Habit.create_habits(molsou)

    navigation = questionary.select("Select one of the following:",
                                    choices=[
                                        "Check off existing habits",
                                        "Create new habits",
                                        "Modify existing habits",
                                        "Delete existing habits",
                                        "Analyze habits or streaks",
                                        "Print all active streaks",
                                        "Exit the application"
                                    ]).ask()

    if navigation == "Exit the application":
        choice = questionary.confirm("Are you sure?").ask()
        if choice == "Yes":
            exit()

    if navigation == "Create new habits":
        name = questionary.text("Habit name: ").ask().lower()
        description = questionary.text("Habit description: ").ask().lower()
        priority = questionary.text("Habit priority: ").ask().lower()
        period = questionary.select("Habit Period: ", choices=["daily", "weekly"]).ask().lower()
        habit_data = Habit(name, description, priority, period)
        Habit.create_habits(habit_data)

    # if navigation == "Delete existing habits":
    #     print(data.get_habits())
    #     habit_to_delete = questionary.text("Type habit to delete: ").ask()
    #     data.remove_habit(habit_to_delete)

    if navigation == "Delete existing habits":
        habit_to_delete = data.select_habit()
        print(habit_to_delete)
        choice = questionary.confirm("Are you sure?").ask()
        if choice == "Yes":
            habit = Habit(habit_to_delete)
            habit.remove_habits()
            # data.remove_habit(habit_to_delete)


    if navigation == "Check off existing habits":
        habit_to_check_off = data.select_habit()
        choice = questionary.confirm("Are you sure?").ask()
        if choice == "Yes":
            habit_data = Habit(habit_to_check_off)
            Habit.completed(habit_data)

