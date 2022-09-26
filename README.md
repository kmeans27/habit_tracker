# habit_tracker
This APP aims to improve your efficiency and let’s you manage and analyze your habits with ease. Currently in development

To run this project follow the following steps:

1. Install python 3.10
2. Install the questionary library for the easy to use command line interface (CLI) //pip install questionary
3. Go to the repository and open a command promt
4. open .\main.py
5. The application should now be open!

By using this APP one can create, delete, complete and analyze habits using a command line interface (questionary)

The app contains 5 classes:
data.py
This class suites as middleman between the database (SQLite3) and the User interface (questionary)
This class has methods to create new habits, delete existing habits and update some columns.

qt.py
This class uses the questionary library to print out some "questions" to the command line interface so the user better knows what to select / enter
It is mostly used to print out some text, so the user has an easier process when creating habits, and to select habits from the sql database to complete/delete/analyze the habits

habit.py
This class creates a habit object and contains the functionality to complete habits.

analytics.py
By using the analytics class the user can simply analyze habits and streaks.

main.py
Main just acts as a dashboard. It shows all the functionality from the app which the user can select by using his arrow keys.
