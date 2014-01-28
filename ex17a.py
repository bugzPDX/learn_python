from sys import argv

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# We could do these two on one line too, how?
indata = open(from_file).read()

open(to_file, 'w').write(indata)

print "Alright, all done."
