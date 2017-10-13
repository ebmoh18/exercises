# Programming Exercise 5-1
#
# Program to convert kilometers to miles.
# This program accepts a distance in kilometers from the user,
# passes it to a function, which calculates its value in miles
# and displays the result for the user.


# Global constant for the ratio of kilometers to miles
Miles_per_KM = 1.60934

def main():
   




# define the main function

    # Define a local float variable to hold the distance in kilometers
    distance = 0.0
    # Get distance in kilometers from the user
    distance = float(input("Enter Distance in Kilometers: "))
    # pass the distance in kilometers to a function to convert to miles

    convert_km_to_miles(distance)

def convert_km_to_miles(distance_in_km):
    distance_in_mi = 0.0
    distance_in_mi = Miles_per_KM * distance_in_km
# define the function to convert to miles
# the function takes kilometers as an argument
# calculates the equivalent number of miles
# and prints the result

    # Define a local float variable for miles

	# use the global conversion constant to compute miles    
    
    # print the results, formatting float values to 2 decimal places
    formated_miles = format(distance_in_mi, '.2f')
    print("You Traveled", formated_miles , "miles")


# Call the main function to start the program
main()
