# Programming Exercise 3-1
#
# Program to display the name of a week day from its number.
# This program prompts a user for the number (1 to 7)
# and uses it to choose the name of a weekday
# to display on the screen.

# Variables to hold the day of the week and the name of the day.
# Be sure to initialize the day of the week to an int and the name as a string.


# Get the number for the day of the week.
# be sure to format the input as an int


# Determine the value to assign to the day of the week.
# use a set of if ... elif ... etc. statements to test the day of the week value.

day = input("Enter the number for the day of the week: ")

if day == 1:
    print("day of the week is Monday")
if day == 2:
    print("day of the week is Tuesday")
if day == 3:
    print("day of the week is Wednesday")
if day == 4:
    print("day of the week is Thursday")
if day == 5:
    print(" day of the week is Friday")
if day == 6:
    print("day of the week is Saturday")
if day == 7:
    print("day of the week is Sunday")

# use the final else to display an error message if the number is out of range.
elif day > 7:
    print("Number Error")
    print("Can't use Number > 7")

# display the name of the day on the screen.




