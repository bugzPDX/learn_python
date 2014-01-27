# This is an additional script for exercise 16
# that reads a file.

from sys import argv

script, filename = argv

print "This file, %r, says..." % filename

target = open(filename)
print target.read()

print "Now I will close the file."
target.close()
