# Programming Exercise 5-3
#
# Program to compute recommended insurance to carry on an item.
# This program accepts a replacement cost from a user,
# calculates a minimum recommended insurance to carry from a global constant,
# then passes these values to a function to be displayed



# Global constant for the percent of replacement cost to insure
global_constant = 0.80
# Define the main function
def main():
    replacement_cost = 0.0
    minimum_insurance = 0.0
    
    # Define local float variables for replacement cost and minimum insurance
    

    # Get the replacement cost from the user
    replacement_cost = float(input("What is the replacement cost: "))
    # Calculate the minimum insurance amount using the global constant
    minimum_insurance = replacement_cost * 0.80
    # Call the function to display the insurance details, 
    
    # passing the replacement cost and minimum insurance to the function
    insurance_details(replacement_cost, minimum_insurance)

      
# Define a function to display the insurance details
def insurance_details(replacement_cost, minimum_insurance):
    

# This function accepts the replacement cost and minimum insurance as parameters,
# uses the global constant to calculate percent insured,
# and displays the insurance details.
    percent_insured = 0.80 * replacement_cost
	# display the replacement cost, formatting the value to 2 decimal places
    print("Replacement Cost =", format(replacement_cost, '.2f'))
    print("Minimum Insurance = ", format(minimum_insurance, '.2f'))
    print("Percent Insurance = ", format(global_constant, '.0%'))
    # display the percent insured, formatting the value to 2 decimal places

	# display the minimum insurance, formatting the value to 2 decimal places


main()
# Call the main function to start the program

