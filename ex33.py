def my_function():
    i = 0
    numbers = []
    max = 20
    increment = int(raw_input('Increment by: '))

    while i <= max:
        print "At the top i is %d" % i
        numbers.append(i)

        i += increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

my_function()
