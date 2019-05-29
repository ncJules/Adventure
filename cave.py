from adventurelib import *

""" adventure specific settings """

Room.items = Bag()

"""define the rooms available, their descriptions and connections"""

hall1 = Room("""You are in Hall 1""")

hall2 = hall1.north = Room("""You are in Hall 2""")

hall3 = hall2.east = Room("""You are in Hall 3""")

hall4 = hall3.north = Room("""You are in Hall 4""")

hall5 = hall4.east = Room("""You are in Hall 5""")

storage1 = hall1.east = Room("""You are in Storage 1""")

storage2 = hall5.east = Room("""You are in Storage 2""")

sleeping = hall3.east = Room("""You are in Sleeping""")

secret1 = storage1.east = Room("""You are in Secret 1""")

secret2 = sleeping.south = Room("""You are in Secret 2""")



"""define the items available and where to find them"""

brush = Item('brush','brush')
sleeping.items = Bag({brush,})



""" Define special actions"""

@when('brush hair')
def brush_hair():
    obj = inventory.find('brush')
    if obj:
        say("Your hair is brushed now, you look like a princess!")
    else:
        say('You do not have a brush.')

        """ Init values"""

current_room = hall1

inventory = Bag()

UsedSteps = 0