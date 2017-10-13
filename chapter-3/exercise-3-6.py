# Programming Exercise 3-6
#
# Program to check if a date is 'magic' (day * month = year).
# This program takes a month, day and year from the user as integers,
# Checks to see if each is in range, then checks whether month * day = year,
# then displays an appropriate message depending on the result

# Variables for month, day, year and message
# initialize month, day and year as integers, message as a string
month = 0
year = 0
day = 0
message = ""



# Get month and cast it to int
month = input("Enter the month: ")
year = input("Enter the year: ")
day = input("Enter the day: ")
# Get day and cast it to int
month = int(month)
year = int(year)
day = int(day)
message = str(message)
# Get year and cast it to int

# This problem can be solved with if-else logic by the reducing the problem domain
# if month input is out of range
if month > 12:
    print("Invalid Month")

	# set message to hold "invalid month" message


# else if day input is out of range
if day > 31:
    print("Invalid day")
    # set message to hold "invalid day" message
    
# else if  year input is out of range (greater than 99 or less than 0)
if 99<year or year<0:
    print("Invalid year")
    # set message to hold "invalid year" message

# else 
elif year == day * month:
    print("Magic Date")
    # set message to hold the date in 00/00/00 form
    messages = str(month) + "/" + str(day) + "/" + str(year)
    print(messages)
    # if day * month equals year, add " is a magic date" to message
else:
    print("Not a Magic Date")
    
    # else add " is not a magic date" to message


# print message for the user


