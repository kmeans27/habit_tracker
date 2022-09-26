import data
from datetime import datetime


class Habit:

    def __init__(self, name: str = None, periodicity: str = None, priority: str = None):
        """

        :param name: Name of the habit
        :param periodicity: Periodicity of the habit
        :param priority: Priority of the habit
        """
        self.name = name
        self.periodicity = periodicity
        self.priority = priority
        self.data = data.connect_database()
        self.streak = 0
        self.current_time = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.completed = False
        self.streak = 0

    def add(self):
        """
        Adds a habit to the "habits" and "events" table. Basically just uses the sophisticated functions from data.py
        :return:
        """
        data.add_habit(self.data, self.name, self.periodicity, self.priority, self.current_time, self.streak)
        data.update_events(self.data, self.name, self.completed, self.streak, self.current_time)

        print(f"\n Added habit name:'{self.name}' with periodicity: '{self.periodicity}' "
                  f"and priority: '{self.priority}' added successful! \n")

    def remove(self):
        """
        Removes a habit from the "habits" and "events" table. Uses the sophisticated functions from data.py
        :return:
        """
        data.remove_habit(self.data, self.name)

        print(f"\nDeleted: '{self.name}'\n")

    def reset_streak(self):
        """
        Sets a habits streak to 1 in the "events" and "habits" table. Uses the sophisticated functions from data.py
        :return:
        """
        self.streak = 1
        data.update_habit_streak(self.data, self.name, self.streak, self.current_time)
        data.update_events(self.data, self.name, False, data.get_streak_count(self.data, self.name), self.current_time)

        print(f"Your streak for Habit: '{self.name}' is now {self.streak}\n")

    def increment_streak(self):
        """
        Increases a habits streak by 1. Uses the sophisticated functions from data.py
        :return:
        """
        self.streak = data.get_streak_count(self.data, self.name)
        self.streak += 1

    def update_streak(self):
        """
        Uses increment_streak(self) to update a habits streak in the "events" and habits" table. Uses the sophisticated functions from data.py
        :return:
        """
        self.increment_streak()
        data.update_habit_streak(self.data, self.name, self.streak, self.current_time)
        data.update_events(self.data, self.name, True, data.get_streak_count(self.data, self.name), self.current_time)

        print(f"\nYour streak for Habit: '{self.name}' is {self.streak}\n")

    def complete(self):
        """
        Marks a habit as completed. Uses the sophisticated functions from data.py
        The function firstly checks the periodicity of the habit to know how to work with the data
        :return:
        """
        if data.get_period(self.data, self.name) == "daily":

            if self.daily_streak() == 0:
                print("\nAlready completed today!\n")
            elif self.daily_streak() == 1:
                self.update_streak()

            else:
                self.reset_streak()

        elif data.get_period(self.data, self.name) == "weekly":
            if self.weekly_streak() == 1:
                print("\nAlready completed this week!\n")
            elif self.weekly_streak() == 2:
                self.update_streak()
            else:
                self.reset_streak()

    def daily_streak(self):
        """
        Returns the days between the last completion time of a habit
        :return: Number of days since last complete
        """
        last = data.get_habit_completion_time(self.data, self.name)
        old_streak = data.get_streak_count(self.data, self.name)
        if old_streak == 0 or last is None:
            return 1

        else:
            today = self.current_time
            date = datetime.strptime(today[:10], "%d/%m/%Y") - datetime.strptime(last[:10], "%d/%m/%Y")
            return date.days


    def weekly_streak(self):
        last = data.get_habit_completion_time(self.data, self.name)
        old_streak = data.get_streak_count(self.data, self.name)
        if  old_streak == 0 or last is None:
            return 2
        else:
            today = self.current_time
            date = datetime.strptime(today[:10], "%d/%m/%Y") - datetime.strptime(last[:10], "%d/%m/%Y")
            week = 3 if date.days > 14 else (2 if date.days > 7 else 1)
            return week



