# function to calculate the area of a triangle


def tri_area(a, b, c):
    # calculate the semi-perimeter
    s = (a + b + c) / 2

    # calculate the area
    my_area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return my_area

# Determine if input is a valid triangle. scalene, isoceles,
# equilateral - obtuse, right, acute


def is_triangle():

    a = 0
    b = 0
    c = 0
# get user input
    a = int(raw_input("Triangle side one? "))
    b = int(raw_input("Triangle side two? "))
    c = int(raw_input("Triangle side three? "))

# sort the input in ascending order
    [a, b, c] = sorted([a, b, c])

# calculate the area of the triangle
    the_area = tri_area(a, b, c)

# determine if input is valid. If valid, calculate triangle type.
    if (a <= 0 or b <= 0 or c <= 0):
        print "\nIllegal sides! Try again.\n"
        is_triangle()

    elif (a + b < c or a + c < b or b + c < a):
        print "\nSides won't reach! Try again.\n"
        is_triangle()

# determines whether all sides are equal
    elif a == b and b == c:
        print ("\nThis is an equilateral triangle with equal "
               "sides of %i units") % a

# determines whether two sides are equal
    elif a == b or a == c or b == c:
        print ("\nThis is an isoceles triangle with sides of "
               "%i, %i and %i units") % (a, b, c)

    else:
        print ("\nThis is a scalene triangle with sides of "
               "%i, %i and %i units") % (a, b, c)

# determine type of triangle.
    if c**2 == a**2 + b**2:
        print "It is also a right triangle."

    elif c**2 < a**2 + b**2:
        print "It is also an acute triangle."

    else:
        print "It is also an obtuse triangle."

    print "The area is %0.2f square units" % the_area
is_triangle()
