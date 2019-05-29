import random

from cave import *


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
        increaseSteps()
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
        increaseSteps()
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
        increaseSteps()

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


""" Mostly useless functions """

def increaseSteps():
    global UsedSteps
    UsedSteps = UsedSteps + 1

@when('steps')
def steps():
    say('It took you %i action(s) to get this far.' % UsedSteps)

@when('hi')
def hi():
    RandomNumber = random.randint(1,11)
    if RandomNumber < 4: 
        say('Well, hello there!')
    elif RandomNumber <6:
        say('Greetings, traveller.')
    elif RandomNumber == 6:
        say('Welcome!')
    else:
        say('Hi, how nice of you to join this adventure!')