
from habit import Habit
import questionary
from datetime import datetime

print("Hello! This APP aims to improve your efficiency and "
      "let’s you manage and analyze your habits with ease. ")



if __name__ == '__main__':
    navigation = questionary.select("Select one of the following:",
                                    choices=[
                                        "Check of existing habits",
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
        else:
            pass

    if navigation == "Create new habits":
        name = questionary.text("Habit name: ")
        description = questionary.text("Habit description: ")
        priority = questionary.text("Habit priority: ")
        period = questionary.text("Habit period: ")
        habit = Habit(name, description, priority, period)
        habit.create_habits()




















