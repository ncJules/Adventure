from adventurelib import *

""" adventure specific settings """

Room.items = Bag()

"""define the rooms available, their descriptions and connections"""

current_room = bath_room = Room("""
You are in the bath room. 
""")

living_room = bath_room.north = Room("""
You enter the living room.
""")

kitchen = living_room.west = Room("""
You are now in the kitchen. It smells nice...
""")

"""define the items avilable and where to find them"""

brush = Item('brush','brush')
bath_room.items = Bag({brush,})

inventory = Bag()

UsedSteps = 0

""" Define special actions"""

@when('brush hair')
def brush_hair():
    obj = inventory.find('brush')
    if obj:
        say("Your hair is brushed now, you look like a princess!")
    else:
        say('You do not have a brush.')