# Had trouble understanding why % not (True and False) was
# invalid syntax. % binds to not before anything so more
# parens are needed.

# Determine result of logic combinations

print 'True and True is %r' % (True and True)
print 'False and True is %r' % (False and True)
print '1 == 1 and 2 == 1 is %r' % (1 == 1 and 2 == 1)
print '"test" == "test" is %r' % ("test" == "test")
print '1 == 1 or 2 != 1 is %r' % (1 == 1 or 2 != 1)
print 'True and 1 == 1 is %r' % (True and 1 == 1)
print 'False and 0 != 0 is %r' % (False and 0 != 0)
print 'True or 1 == 1 is %r' % (True or 1 == 1)
print '"test" == "testing" is %r' % ("test" == "testing")
print '1 != 0 and 2 == 1 is %r' % (1 != 0 and 2 == 1)
print '"test" != "testing" is %r' % ("test" != "testing")
print '"test" == 1 is %r' % ("test" == 1)
print 'not (True and False) is %r' % (not (True and False))
print 'not (1 == 1 and 0 != 1) is %r' % (not (1 == 1 and 0 != 1))
print 'not (10 == 1 or 1000 == 1000) is %r' % (not (10 == 1 or 1000 == 1000))
print 'not (1 != 10 or 3 == 4) is %r' % (not (1 != 10 or 3 == 4))
print 'not ("testing" == "testing" and "Zed" == "Cool Guy") is %r' % (
    not ("testing" == "testing" and "Zed" == "Cool Guy"))
print '1 == 1 and not ("testing" == 1 or 1 == 0) is %r' % 1 == 1 and not (
    "testing" == 1 or 1 == 0)
print '"chunky" == "bacon" and not (3 == 4 or 3 == 3) is %r' % (
    "chunky" == "bacon" and not (3 == 4 or 3 == 3))
print '3 == 3 and not ("testing" == "testing" or "Python" == "Fun") is %r' % (
    3 == 3 and not ("testing" == "testing" or "Python" == "Fun"))
