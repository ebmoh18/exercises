# Programming Exercise 3-2
#
# Program to find which of two rectangles has the greater area.
# This program will get two sets of lengths and widths from a user,
# use them to calculate and compare two area values,
# and display a message comparing those areas

# Local variables
# you need length, width and area for A and for B
# initialize these as floats
a_width = 0.0
a_length = 0.0
a_area = 0.0

b_width = 0.0
b_length = 0.0
b_area = 0.0

# Get length A from the user and convert it to a float
a_width = input("What is the length of Rectangle a: ")
a_length = input("what is the width of Recangle a: ")
b_length = input("What is the lenght of Rectangle b: ")
b_width = input("What is the length of Rectangle b: ")


# Get width A from the user and convert it to a float
a_length = float(a_length)
a_width = float(a_width)
b_length = float(b_length)
b_width = float(b_width)

# Get length B from the user and convert it to a float


# Get width B from the user and convert it to a float


# Calculate area A
a_area = a_length * a_width
a_area = ("%.2f" % a_area)

# Calculate area B
b_area = b_length * b_width
b_area = ("%.2f" % b_area)
# Print each area, formatting the values to 2 decimal places
# if area A is greater, print "A is greater" message.
print("Rectangle A = " , a_area)
print("Rectangle B = " , b_area)

if a_area > b_area:
    print("Rectangle A is greater than Rectangle B")
elif b_area > a_area:
    print("Recangle B is greater than rectangle A")
# else if area B is greater, print "B is greater" message.

# else print "A and B are equal" message.
else:
    print("Recangle A and B are Equal")
