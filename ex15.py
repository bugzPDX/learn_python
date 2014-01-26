# Imports argv for use in this script
from sys import argv

# Sets script and filename variables to values obtained from argv
script, filename = argv

# Sets variable txt equal to a pointer to whatever file was
# entered on the command line.
txt = open(filename)

# Prints the string with the formatted variable
print "Here's your file %r:" % filename
# Prints the content of the file contained in variable txt
print txt.read()

# Prints the string
print "Type the filename again:"
# Sets variable equal to user input
file_again = raw_input("> ")

# Sets variable equal to contents of previous user input
txt_again = open(file_again)

# Prints the content of the data contained in txt_again variable
print txt_again.read()

# Closes txt file
txt.close()
# Closes txt_again file
txt_again.close()
