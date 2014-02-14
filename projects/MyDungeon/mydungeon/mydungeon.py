# Classes file

from random import choice
from textlist import text_list


class Dungeon(object):

    def __init__(self, x, y):

        self.rooms = []
        self.cur_x = 0
        self.cur_y = 0

        for i in range(0, x):
            self.rooms.append([])
            for j in range(0, y):
                self.rooms[i].append(None)

    def add_room(self, x, y, room):

        self.rooms[x][y] = room

    def north(self, args=[]):
        self.go(['north'])

    def south(self, args=[]):
        self.go(['south'])

    def east(self, args=[]):
        self.go(['east'])

    def west(self, args=[]):
        self.go(['west'])

    def go(self, args):
        direction = args[0]

        x = self.cur_x
        y = self.cur_y

        if direction == "north":
            if y == len(self.rooms[x]) - 1:
                print "You can't go that way."
            else:
                y += 1

        elif direction == "south":
            if y == 0:
                print "You can't go that way"
            else:
                y -= 1

        elif direction == "east":
            if x == len(self.rooms) - 1:
                print "You can't go that way."
            else:
                x += 1

        elif direction == "west":
            if x == 0:
                print "You can't go that way"
            else:
                x -= 1
        else:
            print "I don't know what that means."

        if self.rooms[x][y]:
            self.cur_x = x
            self.cur_y = y
            self.room().enter()
        else:
            print "You can't go that way."
        return self.room()

    def room(self):
        return self.rooms[self.cur_x][self.cur_y]


class Room(object):

    def __init__(self, name="Kitchen"):

        self.name = name
        self.__inventory = {}

    def enter(self, args=[]):

        print "You are in the %s" % self.name

    def look(self, args=[]):
        self.enter()
        if self.__inventory:
            print "You see %s lying on the floor" \
                % text_list(self.__inventory.values())
        else:
            return

    def fight(self, args=[]):
        print "You take a swing but there is nothing to fight"

    def add_item(self, item_name, item_description):
        self.__inventory[item_name] = item_description

    def take_item(self, item_name):
        if item_name in self.__inventory:
            item_description = self.__inventory[item_name]
            del self.__inventory[item_name]
            return item_description
        return None


class MonsterRoom(Room):

    def __init__(self, monster, name="Monster Room"):

        self.monster = monster
        super(MonsterRoom, self).__init__(name)

    def enter(self, args=[]):

        super(MonsterRoom, self).enter()
        if self.monster:
            print "There is a %s here!" % self.monster

    def fight(self, args=[]):
        if not self.monster:
            print "There is nothing to fight here."
            return
        if choice([True, False]):
            print "You win!"
            self.monster = None
        else:
            print "You lose!"
            print "That was a ridiculously short game."
            user_command = raw_input("Play again? ").lower()
            if user_command == "yes":
                start()
            else:
                exit(0)


class Character(object):

    def __init__(self, c_name):
        self.name = c_name
        self.__inventory = \
            {"hat": "a knit hat",
             "mittens": "a pair of mittens", "key": "a brass key"}
        self.__dungeon = None

    def inventory(self, args=[]):
        print "You have %s" % text_list(self.__inventory.values())

    def enter_dungeon(self, dungeon):

        print "Welcome %s! You find yourself standing in a strange " \
            "%s." % (self.name, dungeon.room().name)
        self.__dungeon = dungeon

    def drop(self, args=[]):
        item_name = args[0]
        if item_name in self.__inventory:
            item_description = self.__inventory[item_name]
            print "You have dropped the %s." % item_name
            self.__dungeon.room().add_item(item_name, item_description)
            del self.__inventory[item_name]
        else:
            print "You don't have that."

    def get(self, args=[]):
        item_name = args[0]
        item_description = self.__dungeon.room().take_item(item_name)
        if item_description:
            print "You picked up %s." % item_description
            self.__inventory[item_name] = item_description
        else:
            print "I don't see %s." % item_name


class Adventurer(Character):

    def __init__(self, a_name):
        if not a_name:
            print "No name huh? I guess you will be " \
                "called Emanon"
            a_name = "Emanon"

        super(Adventurer, self).__init__(a_name)


class Monster(Character):

    pass

my_adventurer = None
my_dungeon = None

# This is where things start happening.


def start():
    global my_adventurer
    global my_dungeon
    my_adventurer = Adventurer(raw_input("What is your name, Adventurer? "))
    dark_room = Room("Dark Room")
    dark_room.add_item("lamp", "a brass lamp")
    my_dungeon = Dungeon(3, 3)
    my_dungeon.add_room(0, 0, Room())
    my_dungeon.add_room(0, 1, MonsterRoom("Grue", "Dining Room"))
    my_dungeon.add_room(0, 2, dark_room)
    my_dungeon.add_room(1, 2, Room("Bedroom"))
    my_dungeon.add_room(2, 2, Room("Closet"))
    my_dungeon.add_room(2, 1, Room("Secret Passage"))
    my_dungeon.add_room(2, 0, Room("Hidden Room"))
    my_adventurer.enter_dungeon(my_dungeon)
start()

while True:
    print "Your coordinates are %s, %s" % (my_dungeon.cur_x, my_dungeon.cur_y)

    args = raw_input("> ").lower().split(' ')
    method = args.pop(0)

    has_error = True
    for obj in (my_adventurer, my_dungeon.room(), my_dungeon):
        try:
            getattr(obj, method)(args)
            has_error = False
            break
        except AttributeError:
            pass

    if has_error:
        print "Not sure what you mean"
