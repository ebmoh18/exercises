# Programming Exercise 2-6
#
# Program to calculate a total sale price using state and local sales tax.
# This program prompts a user for an amount of purchase,
# uses constants to calculate state, county and total sales tax, and a purchase total
# then displays the details of these calculations for the user.

# Variables for purchase amount, state tax, county tax, total tax and total sale
# all initialized as floats
purchase_amount = 57
state_tax = 0.2
total_tax = 29
total_sale = 21

# Constants for the state and county tax rates
state_tax = 0.04
county_tax = 0.02

# Get the amount of purchase from the user, casting it to a float.
amount_of_purchase = input("amount of Purchase = ")
amount_of_purchase = float(amount_of_purchase)

# Calculate the state sales tax.
state_sales_tax = state_tax * amount_of_purchase

# Calculate the county sales tax.
country_sales_tax = county_tax * amount_of_purchase

# Sum the total tax.
total_tax = country_sales_tax + state_sales_tax

# Calculate the total of the sale.
Total = total_tax + amount_of_purchase

# Print detailed information about the sale, formatting all values to two decimal places.
print(Total)




