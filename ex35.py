from sys import exit
DEBUG = False
## :g/DEBUG/d


def text_list(listtext, sep1=", ", sep2=", and "):
    n = len(listtext)
    if n > 1:
        return sep1.join(listtext[:-1]) + sep2 + listtext[-1]
    else:
        return listtext[0]


def troll_shop(how_much):
    print """You have wandered into a troll shop. Good thing you grabbed
    some gold! A stinky troll greets you with a grunt.
    Do you want to [shop] or [leave]?"""

    user_command = raw_input("> ")
    if user_command == "shop":
        print """You browse the shop and see a small, purple
        glass [bottle] containing some sort of liquid,
        A rusty [sword] with a broken edge, a wooden [box]
        closed with a lock and an empty cloth [bag]."""
        print """The troll seems irritated. It wants to
        know what you want to buy. Maybe you want to
        know the [prices]"""

        inventory = {"bottle": 6, "sword": 10, "box": 40, "bag": 30}
        backpack = []

        while how_much > 0 and len(inventory):

            user_command = raw_input("> ")
            if user_command == "leave":
                break
            elif user_command == "prices":
                for i in inventory:
                    print "The %s is %s" % (i, inventory[i])
                print "What do you want to [buy]?"
            else:
                action, item = user_command.split()
                if action == "buy":
                    if item in inventory:
                        cost = inventory[item]
                        how_much -= cost
                        backpack.append(item)
                        del inventory[item]
                        print "Thanks! You now have a %s" % item
                    else:
                        print "We don't have a %s" % item
                        print "We have %s" % text_list(inventory.keys())
                else:
                    print "Whaddya want already?!"

        print "Well that was interesting but now the game is over."
        print ("You ended up with a %s.You have %s gold"
               "remaining.") % (text_list(backpack), how_much)
        exit()

    else:
        print """Great, you angered the troll. Now it just wants you to
        give it all of your gold. Do you want to [give] it up
        or try to [run]?"""

        user_command = raw_input("> ")
        if user_command == "give":
            print "Wise choice! You are broke but you get to live!"
            dead("This was a pretty short adventure.")

        else:
            dead("""You weren't fast enough. The troll killed you
            with that rusty sword.""")


def gold_room():
    print "This room is full of gold coins. What number of coins do you take?"

    user_command = raw_input("> ")
    if user_command.isdigit():
        how_much = int(user_command)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy"
        troll_shop(how_much)
    else:
        dead("You greedy bastard!"
             " You caused an avalanche of coins and now you are dead!")


def bear_room():
    print """There is a bear here.
    The bear has a bunch of honey.
    The fat bear is in front of another door.
    How are you going to move the bear?
    [take honey] or [taunt bear]?"""
    bear_moved = False

    while True:
        user_command = raw_input("> ").lower()

        if user_command == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif user_command == "taunt bear" and not bear_moved:
            print "The bear has moved from the door."\
                " You can go through it now. [taunt bear] or [open door]?"
            bear_moved = True
        elif user_command == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif user_command == "open door" and bear_moved:
            gold_room()
        else:
            print "I have no idea what that means."


def cthulhu_room():
    print """Here you see the Dark Lord Cthulhu.
    He, it, whatever stares at you and you go insane.
    Do you [flee] for your life or [eat] your head?"""

    user_command = raw_input("> ").lower()

    if "flee" in user_command:
        start()
    elif "eat" in user_command:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    user_command = raw_input("Play again? ").lower()
    if user_command == "yes":
        start()
    else:
        exit(0)


def start():
    print """You are in a dark room.
    There is a door to your right and left.
    Which one do you take? [Left] or [right]?"""

    user_command = raw_input("> ").lower()

    if user_command == "left":
        bear_room()
    elif user_command == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
