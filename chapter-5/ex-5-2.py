# Programming Exercise 5-2
#
# Program to calculate final purchase details.
# This program takes a purchase amount from a user,
# then calculates state tax, county tax and total tax,
# 	and passes them to a function to be totaled
# and displayed



# Global constants for the state and county tax rates
state_tax = 0.06

county_tax = .06
# define the main function
def main():

    # Define local float variables for purchase, state tax and county tax
    purchase = 0.0
    state_tax = 0.06
    county_tax = .06
    # Get the purchase amount from the user
    purchase = float(input("What is the purchase total: "))
    # Calculate the state tax using the global constant for state tax rate
    state_tax_calculation = purchase * 0.06
    # Calculate the county tax using the global constant for county tax rate
    county_tax_calculation = purchase * .06
    # Call the sale details function, passing the purchase, state tax and county tax
    


# define a function to display purchase details
# this function accepts purchase, stateTax, and countyTax as arguments,
# calculates the total tax and sale total,
# then displays the purchase details

    # Define local float variables for total tax and sale total

	# Calculate the total tax
    total_tax = state_tax_calculation + county_tax_calculation
	# Calculate the total sale
    total_sale = total_tax + purchase
    # Display the purchase details, including purchase, state tax, county tax,
    #	total tax, and sale total, each on a line.  Format floats to 2 decimal places.
    formated_a = format(purchase, '.2f')
    formated_b = format(state_tax_calculation, '.2f')
    formated_c = format(county_tax_calculation, '.2f')
    formated_d = format(total_sale, '.2f')
    
    print("Purchase Total = ", formated_a)
    print("State Tax = ", formated_b)
    print("County Tax = ", formated_c)
    print("Total Sale = ", formated_d)
    

main()
# Call the main function to start the program.

