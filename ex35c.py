# Classes file


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

    def go(self, direction):

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
        else:
            print "You can't go that way."
        return self.room()

    def room(self):
        return self.rooms[self.cur_x][self.cur_y]


class Room(object):

    def __init__(self, description="A room"):

        self.description = description


my_room = Room()
print my_room.description

my_dungeon = Dungeon(3, 3)
my_dungeon.add_room(0, 0, my_room)

my_dungeon.add_room(0, 1, Room("Another room"))
print my_dungeon.rooms[0][1].description

my_dungeon.add_room(0, 2, Room("Dark Room"))
my_dungeon.add_room(1, 2, Room("Bedroom"))
my_dungeon.add_room(2, 2, Room("Closet"))
my_dungeon.add_room(2, 1, Room("Secret Passage"))
my_dungeon.add_room(2, 0, Room("Hidden Room"))

while True:
    print "You are in %s" % my_dungeon.room().description
    print "Your coordinates are %s, %s" % (my_dungeon.cur_x, my_dungeon.cur_y)
    command = raw_input("> ")
    my_dungeon.go(command)
