# Programming Exercise 3-5
#
# Program to convert a value in kilograms to Newtons, then check whether it is in range.
# This program will prompt a user for a mass in kilograms,
# convert it to Newtons and use constants to check if the weight is within range,
# then display the weight and a range message.



# Global constants for minimum, maximum and mass multiplier values
Constant = 9.81

# Variables for weight and mass initialized as floats   


# Get mass from user and convert it to a float
mass = input("Enter the mass in Kilograms: ")
mass = float(mass)

# Calculate weight using the mass multiplier constant
mass_in_newtons = mass * 9.81
mass_in_newtons = str(mass_in_newtons)
print("Mass In Newtons = " + mass_in_newtons + " Newtons")

# Display the weight

# If weight > maximum or < than minimum display an appropriate message








