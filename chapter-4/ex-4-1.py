# Programming Exercise 4-1
#
# Program to total the values of five integers.
# This program the user for an integer five times,
# and totals them up,
# then displays the total entered on the screen.

# Initialize variables for bugs collected and total bugs.
# be sure to initialize them as integers


# Get the number of bugs collected from the user
# use a for loop to get the number of bugs exactly five times, once for each day
day1 = input("Bugs collected in day one: ")
day2 = input("Bugs collected in day two: ")
day3 = input("Bugs collected in day three: ")
day4 = input("Bugs collected in day four: ")
day5 = input("Bugs collected in day five: ")
	# input bugs collected on this day and convert it to an int
day1 = int(day1)
day2 = int(day2)
day3 = int(day3)
day4 = int(day4)
day5 = int(day5)
    
    # add bugs collected to total bugs
Total_Bugs_Collected = day1 + day2 + day3 + day4 + day5

# Display the total number of bugs collected for all five days.
print("Total Bugs Collected = " , Total_Bugs_Collected)