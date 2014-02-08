## Animal is-a object (yes, sort of confusing) look at the extra credit


class Animal(object):

    def __init__(self, name):
        ## animal has-a name
        self.name = name

## Dog is-a Animal


class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name


## Cat is-a Animal

class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name


class Person(object):

    def __init__(self, xname):
        ## Person has-a name
        self.name = xname

        ## Person can has-a pet of some kind
        self.pet = None

    def say_hi(self):
        print "Hi!"


## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee name is referenced from super class Person.
        ## hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

my_employee = Employee("Bob", 50000)
my_employee.say_hi()


## Fish is-a object
class Fish(object):
    pass
    ##def __init__(self, gills, scales):
        ### Fish has-a gills
        #self.gills = gills
        #self.scales = scales


## Salmon is-a fish
class Salmon(Fish):

    def __init__(self, name):
    ## Salmon has-a name
        self.name = name


class Halibut(Fish):

    def __init__(self, name):
        ## Halibut has-a name
        self.name = name


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon("joe")

## harry is-a Halibut
harry = Halibut("sam")

harry.mom = "Cindy"
print "Hi %s!" % harry.mom
print harry
