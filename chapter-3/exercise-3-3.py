# Programming Exercise 3-3
#
# Program to assign an age category to an numerical age.
# This program will prompt the user for an integer age value,
# and use it to choose an age category,
# then display that category on the screen.

# Variables to hold an age and a category.
# initialize age as an int and category as a string.
age = input("How Old Are You: ")
# Get the person's age.
# remember to convert the input to an int.
age = int(age)
if age <=1:
    print("Infant")
elif 1<age<13:
    print("Child")
elif 13<=age<19:
    print("Teenager")
elif age>18:
    print("Adult")
# Determine if the person is an infant, child, teenager, or adult and set the category.
# Use a series of if ... elif ... etc. statements.





# display a message with the age category.



