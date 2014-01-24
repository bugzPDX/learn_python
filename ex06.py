# Set variable x equal to string containing formatted variable
x = "There are %d types of people." % 10
# Set variable binary equal to string
binary = "binary"
# Set variable do_not equal to string
do_not = "don't"
# Set variable y equal to string containing two formatted variables
y = "Those who know %s and those who %s." % (binary, do_not)

# Prints strings and formatted variables that x and y are set to
print x
print y

# Prints strings and formatted variables x and y
print "I said: %r." % x
print "I also said: '%s'." % y

# Sets variable hilarious equal to False
hilarious = False
# Sets variable joke_evaluation equal to a string containing formatted variable
joke_evaluation = "Isn't that joke so funny?! %r"
# Prints string and the formatted variable hilarious
print joke_evaluation % hilarious

# Sets variables w and e equal to strings
w = "This is the left side of..."
e = "a string with a right side."

# Prints the concatenated strings of variables w and e
print w + e
