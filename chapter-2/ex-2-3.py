# Programming Exercise 2-3
#
# Program to convert area in square feet to acres.
# This program will prompt a user for the size of a tract in square feet,
# then use a constant ratio value to calculate it value in acres
# and display the result to the user.

# Variables to hold the size of the tract and number of acres.
# be sure to initialize these as floats
size_of_tract = 3
number_of_acres = 2.2957e-5

# Constant for the number of square feet in an acre.

# Get the square feet in the tract from the user.
# you will need to convert this input to a float
size_of_tract = input("size_of_tract =")
size_of_tract = float(size_of_tract)
# Calculate the number of acres.
total_number_of_acres= size_of_tract * number_of_acres



# Print the number of acres.
# remember to format the acres to two decimal places
print(total_number_of_acres)



