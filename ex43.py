from sys import exit
from random import randint

class Game(object):

	def __init__(self, start):
		self.quips = [
			"You died. You kinda suck at this.",
			"Your mom would be proud. If she were smarter.",
			"Such a loser.",
			"I have a small puppy that's better at this."
		]
		self.start = start
	
	def play(self):
		next_room_name = self.start
		
		while True:
			print "\n--------"
			room = getattr(self, next_room_name)
			print room.__doc__
			action = raw_input("> ")
			next_room_name = room(action)
			
	def death(self, action):
		print self.quips[randint(0, len(self.quips)-1)]
		exit(1)
		
	def central_corridor(self, action):
		 """The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew. You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the bridge, and blow the ship up after getting into an escape pod.
\n
You're running down the central corridor to the Weapons Armory when
a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
flowing around his hate filled body. He's blocking the door to the
Armory and about to pull a weapon to blast you."""
		
		
		if action == "shoot!":
			print """Quick on the draw you yank out your blaster and fire it at the Gothon.
His clown costume is flowing and moving around his body, which throws
off your aim. Your laser hits his costume but misses him entirely. This
completely ruins his brand new costume his mother bought him, which
makes him fly into an insane rage and blast you repeatedly in the face until
you are dead. Then he eats you."""
			return 'death'
			
		elif action == "dodge!":
			print """Like a world class boxer you dodge, weave, slip and slide right
as the Gothon's blaster cranks a laser past your head.
In the middle of your artful dodge your foot slips and you
bang your head on the metal wall and pass out.
You wake up shortly after only to ddie as the Gothon stomps on
your head and eats you."""
			return 'death'
			
		elif action == "tell a joke":
			print """Lucky for you they made you learn Gothon insults in the academy.\n
You tell the one Gothon joke you know:
Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf neghaq gur ubhfr\n
The Gothon stops, tries not to laugh, then busts out laughing and can't move.
While he's laughing you run up and shoot him square in the head
putting him down, then jump through the Weapon Armory door."""
			return 'laser_weapon_armory'
			
		else:
			print "DOES NOT COMPUTE!"
			return 'central_corridor'
			
	def laser_weapon_armory(self, action):
		"""You do a dive roll into the Weapon Armory, crouch and scan the room
for more Gothons that might be hiding. It's dead quiet, too quiet.
You stand up and run to the far side of the room and find the
neutron bomb in its container. There's a keypad lock on the box
and you need the code to get the bomb out. If you get the code
wrong 10 times then the lock closes forever and you can't
get the bomb. the code is 3 digits."""
		code = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9))
		print code
		guess = 0 #raw_input("[keypad]> ")
		guesses = 0
		
		while guess != code and guesses < 10:
			guesses += 1
			guess = raw_input("[keypad]> ")
			print "BZZZZZZZEDDD!"
			
		if guess == code:
			print """The container clicks open and the seal breaks, letting gas out.
You grab the neutron bomb and run as fast as you can to the
bridge where you must place it in the right spot."""
			return 'the_bridge'
		else:
			print """The lock buzzes one last time and then you hear a sickening
melting sound as the mechanism is fused together.
You decide to sit there, and finally the Gothons blow up the
ship from their ship and you die."""
			return 'death'
			
	def the_bridge(self, action):
		"""You burst onto the Bridge with the netron destruct bomb
under your arm and surprise 5 Gothons who are trying to
take control of the ship. Each of them has an even uglier
clown costume than the last. They haven't pulled their.
weapons out yet, as they see the active bomb under your
arm and don't want to set it off."""
				
		if action == "throw the bomb":
			print """In a panic you throw the bomb at the group of Gothons
and make a leap of the door. Right as you drop it a
Gothon shoots you right in the back killing you.
As you die you see another Gothon franticaly try to disarm
the bomb. You die knowing they will probably blow up when
it goes off."""
			return 'death'
			
		elif action == "slowly place the bomb":
			print """You point your blaster at the bomb under your arm
and the Gothons put their hands up and start to sweat.
You inch backward to the door, punch the close button
and blast the lock so the Gothons can't get out.
Now that the bomb is placed you run to the excape pod to
get off this tin can."""
			return 'escape_pod'
			
		else:
			print "DOES NOT COMPUTE!"
			return "the_bridge"
			
	def escape_pod(self, action):
		"""You rush through the ship desperately trying to make it to
the escape pod before the whole ship explodes. It seems like
hardly any Gothons are on the ship, so your run is clear of
interference. You get to the chamber with the escape pods, and
now need to pick one to take. Some of them could be damaged
but you don't have time to look. There are 5 pods. Which one
do you take?"""
		
		good_pod = randint(1, 5)
		print good_pod
		guess = raw_input("[pod #]> ")
		
		if int(guess) != good_pod:
			print """You jump into pod %s and hit the eject button.
The pod escapes out into the void of space, then
implodes as the hull ruptures, crushing your body
into a ball of liquid.""" % guess
			return 'death'
			
		else:
			print """You jump into pod %s and hit the eject button.
The pod easily slides out into space heading to
the planet below. As it flies to the planet, you look
back and see your ship implode then explode like a
bright star, taking out the Gothon ship at the same
time. You won!""" % guess
			exit(0)
			
a_game = Game("central_corridor")
a_game.play()																	