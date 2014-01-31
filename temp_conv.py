# program to convert from Farenheit to Celcius
def f_2_c(temp):
    c = 5.0/9*(temp-32)
    return c

f = -40
while f <= 100:
    C = f_2_c(f)
    print "The temp in F is %i. The temp in C is %i." % (f, C)
    f += 5
