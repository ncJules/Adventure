from adventurelib import *
from genericfunctionslib import *

global current_room

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

""" Define special actions"""

@when('brush hair')
def brush_hair():
    obj = inventory.find('brush')
    if obj:
        say("Your hair is brushed now, you look like a princess!")
    else:
        say('You do not have a brush.')

start()
look()


""" Define all the general stuff """

"""Define the movements between the rooms"""

@when('go north', direction = 'north')
@when('go west', direction = 'west')
@when('go south', direction = 'south')
@when('go east', direction = 'east')
def go (direction):
    global current_room
    room = current_room.exit(direction)
    if room:
        current_room = room
        say('You go %s.' % direction)
        look()
    else:
        say('There is nothing %s of you.' % direction)


"""check you surroundings"""
@when('look')
def look():
    say(current_room)
    if current_room.items:
        say('You see:')
        for i in current_room.items:
            say('* A %s' % i)


"""Define all the item related stuff"""

@when('take THING')
def take(thing):
    obj = current_room.items.take(thing)
    if obj:
        say('You pick up the %s.' % obj)
        inventory.add(obj)
    else:
        say('There is no %s here.' % thing)

@when('drop THING')
def drop(thing):
    obj = inventory.take(thing)
    if not obj:
        say('You do not have a %s.' % thing)
    else:
        say('You drop the %s.' % obj)
        current_room.items.add(obj)

@when('inventory')
def show_inventory():
    if len(inventory) == 0:
        say('You do not have anything...')
    else:
        say('You have:')
        for thing in inventory:
            say(thing)   

@when('check for THING')
def check_inventory_for(thing):
    obj = inventory.find(thing)
    if obj:
        say('You have a %s' % thing)
    else:
        say('You do not have a %s' % thing)