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
    if current_room.characters:
        say("There is somebody in this room.")


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

@when('use THING')
def use(thing):
    """first determine if a single item shall be used or is more shall be combined by checking for the word WITH """
    if thing.count("with",0,len(thing)) == 0:
        obj = inventory.find(thing)
        if obj:
            increaseSteps()
            if 1==0:
                """possible actions shall be added here"""
            else:
                RandomNumber = random.randint(1,11)
                if RandomNumber < 4: 
                    say("There is not much to be done!")
                elif RandomNumber < 6:
                    say("I do not see the value in that.")
                elif RandomNumber < 7:
                    say("But I really don't wanna...")
                else:
                    say("I would love to, but I don't see how.")
        else:
            say("You don't have a %s" % thing)
    else:
        thing1 = thing[:thing.rfind("with")-1]
        thing2 = thing[thing.rfind("with")+5:]
        obj1 = inventory.find(thing1)
        obj2 = inventory.find(thing2)
        if obj1:
            if obj2: 
                increaseSteps()
                if 1==0:
                    """possible actions shall be added here"""
                else:
                    RandomNumber = random.randint(1,11)
                    if RandomNumber < 4: 
                        say("I don't see how.")
                    elif RandomNumber < 6:
                        say("Interesting, but NO.")
                    elif RandomNumber < 7:
                        say("I would love to, but then I would have to kill you...")
                    else:
                        say("But I really don't wanna...")
            else:
                say("You don't have a %s" % thing2)
        else:
            say("You don't have a %s" % thing1)


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