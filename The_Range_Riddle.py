# Objective: The aim of this assignment is to deepen your understanding of Python's range() function.
# Task 1: Your Mood Today 
# Write a program that prints off different moods for each day of the week. Create a list of moods such 
# as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, loop through every day of the week and for each day, randomly 
# select a mood from the list and print it. Ensure that your program includes the use of the random module to select the mood.

import random

moods = ['Happy', 'Sad', 'Energetic', 'Calm']
days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

for day in days_of_the_week:
    mood = random.choice(moods)
    print("It's " + day + " and I'm feeling " + str(mood) + "!")
