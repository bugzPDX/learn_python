class Parent(object):

	def implicit(self):
		print "Parent implicit()"
		print "\n"
		
class Child(Parent):
	pass
	
dad = Parent()
son = Child()

dad.implicit()
son.implicit()




class Parent(object):

    def override(self):
        print "PARENT override()"

class Child(Parent):

    def override(self):
        print "CHILD override()"
        print "\n"

dad = Parent()
son = Child()

dad.override()
son.override()





class Parent(object):

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"
        print "\n"

dad = Parent()
son = Child()

dad.altered()
son.altered()



class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit() # prints PARENT implicit()
son.implicit() # prints PARENT implicit()

dad.override() # prints PARENT override()
son.override() # prints CHILD override()

dad.altered() # prints PARENT altered()
son.altered() # prints CHILD, BEFORE PARENT altered() then PARENT altered() then CHILD AFTER PARENT altered()			