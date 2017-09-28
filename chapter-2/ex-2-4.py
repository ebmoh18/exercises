# Programming Exercise 2-4
#
# Program to compute a final price for five items with tax.
# This program will prompt a user for a set of five prices,
# sum them to a subtotal and calculate sales tax with tax rate stored in a constant,
# then display the results on the screen.

# Variables to hold the prices of five items, the subtotal, and the total.
# All should be initialized as floats.
apples = input("price_of_apples = ")
bananas = input("price_of_bananas = ")
mangos = input("price_of_mangos = ")

# Constant for the sales tax rate.
tax_rate = 0.06 

# Get the price of each item by prompting the user.
# You will need to convert each input to a float.
apples = float(apples)
bananas = float(bananas)
mangos = float(mangos)
# Calculate the subtotal by adding up the item prices.
subtotal = apples + bananas + mangos

# Calculate the sales tax by multiplying the subtotal by the tax rate.
sales_tax = subtotal * tax_rate

# Calculate the total by adding the subtotal and tax.
total = sales_tax + subtotal

# Print the values for the subtotal, tax and total.
# Label each value, and format them to display with two decimal places. 
print(total)




