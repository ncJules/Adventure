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
            say('* %s' % i)
    if current_room.characters:
        say("There is somebody in this room.")

        """ Story related checkpoints """

def init_CPs():
    global CalmDownFundor
    CalmDownFundor = False
    """set to true when you give the letter from Dàin to Fundór"""
    global FundorHasRunepaper
    FundorHasRunepaper = False
    """set to true as soon as the runepaper is given to Fundór"""
    global FundorHasMoonstone
    FundorHasMoonstone = False
    """set to true as soon as the moonstone is given to Fundór"""
    global GotLocationOfKey
    GotLocationOfKey = False
    """set to true after Fundór has deciphered the runepaper"""
    global GotLocationOfDoor
    GotLocationOfDoor = False
    """set to true after Fundór has deciphered the runepaper"""
    global CupboardDestroyed
    CupboardDestroyed = False
    """ is set to true after the cupboard has been chopped down with the axe """
    global LocalisedKey
    LocalisedKey = False
    """ Set to TRUE when you have the bottle and you know that the key is inside"""
    """ if you want to set a checkpoint to true, code: 
        global CP
        CP = True
    """

@when('progress')
def progress():
    say("%s" % CalmDownFundor)
    say("%s" % FundorHasRunepaper)
    say("%s" % FundorHasMoonstone)
    say("%s" % GotLocationOfKey)
    say("%s" % GotLocationOfDoor)
    say("%s" % CupboardDestroyed)
    say("%s" % LocalisedKey)

"""Define all the item related stuff"""
def inventory_is_full():
    number_of_items = 0
    for i in inventory:
        number_of_items = number_of_items + 1
    if number_of_items > 6:
        return True
    else:
        return False

@when('take THING')
def take(thing):
    if inventory_is_full():
        say("Your bag is full, you can't carry anymore!")
    else:
        obj = current_room.items.take(thing)
        if obj:
            say('You pick up %s.' % obj)
            inventory.add(obj)
            increaseSteps()
            if obj == winebottle:          
                if GotLocationOfKey:
                    global LocalisedKey
                    LocalisedKey = True
            if obj == key:
                if CupboardDestroyed:
                    treasure = dining.east = Room("""The key fits inside the small lock... You have finally found the treasure room. But unfortunately it has not been used for a very long time - there's not much to be found.""")
                    treasure.items = Bag({sword,})
            if obj == sword:
                say("Even though the sword is very rusty, you can still see that it's old with dwarfen runes on it. It's most probably worth something!")
                say("Happy to have found the last survivors and your nephew amongst them, you decide that this sword with all the other things you've found in the cave will be enough for delivering to Dáin and you tell the others to pack there things.")
                say("")
                say("You are all going to be home soon...")
                quit()
        else:
            say('There is/are no %s here.' % thing)

@when('drop THING')
def drop(thing):
    obj = inventory.take(thing)
    if not obj:
        say('You do not have (a) %s.' % thing)
    else:
        say('You drop %s.' % obj)
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
        say('You have (a) %s' % thing)
    else:
        say('You do not have (a) %s' % thing)

@when('give THING')
def give(thing):
    obj = inventory.find(thing)
    if thing == "hand":
        say("Nice gesture!")
    elif not obj:
        say('You do not have (a) %s' % thing)
    else:
        if not current_room.characters:
            say('There is no one to give it to.')
        else:
            increaseSteps()
            obj = inventory.take(thing)
            current_room.items.add(obj)
            say('You hand over the %s.' % thing)
            if (thing == 'letter' and current_room.characters.find('Fundor')):
                global CalmDownFundor
                CalmDownFundor = True
            if (thing == 'moonstone' and current_room.characters.find('Fundor')):
                global FundorHasMoonstone
                FundorHasMoonstone = True
            if (thing == 'runepaper' and current_room.characters.find('Fundor')):
                global FundorHasRunepaper
                FundorHasRunepaper = True
            if (thing == 'bottle' and current_room.characters.find('Frain')):
                say("As soon as you hand the bottle to the old dwarf he empties it at an impressive paste. To be sure that it's really empty, he turns it upside down.")
                say("You hear a soft CLONK as a small key drops on to the table in front of you.")
                current_room.items.add(key)
                           
                
@when('use THING')
def use(thing):
    """first determine if a single item shall be used or is more shall be combined by checking for the word WITH """
    if thing.count("with",0,len(thing)) == 0:
        obj = inventory.find(thing)
        if obj:
            increaseSteps()
            if obj == longbow or obj == axe:
                say("What shall I used it with?")
            elif obj == ham:
                say("That was delicious!")
                inventory.remove(ham)
            elif obj == winebottle:
                say("I don't drink alone!")
            elif obj == ring:
                say("An ELVEN ring? Are you serious?")
                """more possible actions shall be added here"""
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
            say("You don't have (a) %s" % thing)
    else:
        thing1 = thing[:thing.rfind("with")-1]
        thing2 = thing[thing.rfind("with")+5:]
        obj1 = inventory.find(thing1)
        obj2 = inventory.find(thing2)
        if obj1:
            global CupboardDestroyed
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
            elif obj1 == axe and thing2 == "cupboard" and current_room == dining and not CupboardDestroyed:
                say("You chop the cupboard until there are only small pieces left. It feels good having something to do with your hands.")
                say("After you have finished this marvellous job, you see a small old door.")
                if not bool(inventory.find('key')):
                    say("If only you had a key for it...")
                CupboardDestroyed = True
                if bool(inventory.find('key')):
                    treasure = dining.east = Room("""The key fits inside the small lock... You have finally found the treasure room. But unfortunately it has not been used for a very long time - there's not much to be found.""")
                    treasure.items = Bag({sword,})
            else:
                say("You don't have (a) %s" % thing2)
        elif thing1 == "cupboard" and obj2 == axe and current_room == dining and not CupboardDestroyed:
            say("You chop the cupboard until there are only small pieces left. It feels good having something to do with your hands.")
            say("After you have finished this marvellous job, you see a small old door.")
            if not bool(inventory.find('key')):
                    say("If only you had a key for it...")
            CupboardDestroyed = True
            if bool(inventory.find('key')):
                treasure = dining.east = Room("""The key fits inside the small lock... You have finally found the treasure room. But unfortunately it has not been used for a very long time - there's not much to be found.""")
                treasure.items = Bag({sword,})
        else:
            say("You don't have (a) %s" % thing1)

"""Define all the character related stuff"""

@when('talk to PERSON')
def talk(person):
    for i in current_room.characters:
        pers = i
    if person == 'myself':
        say("I usually am a fun guy to talk to, but at the moment I am quite tired.")
    elif current_room.characters:
        if person == 'dwarf' or person == 'person' or person == 'somebody' or current_room.characters.find(person):
            increaseSteps()
            if pers == Fundor:
                if not CalmDownFundor:
                    say("I'm loosing my mind in this loneliness! If only I could get a word from the Erebor and my beloved king once again ...")
                elif not (FundorHasMoonstone or FundorHasRunepaper):
                    say("Hello and thank you for showing me the letter from Dàin. It is good to know that we were not forgotten at the kingdom of Erebor.")
                    say("My name is Fundór and I am one of the historians sent to Khazad-dûm. I specialised on old dwarfen runes but my task was mainly to identify the old items found in the mines.  ")
                    say("As I read in your letter, you are not only searching for survivors but also for items.")
                    say("If you promise to take me back home to the Erebor, I will be happy to help you with whatever you may need.")
                elif (FundorHasMoonstone and current_room.items.find('moonstone') and not FundorHasRunepaper):
                    say("This gem I rescued from the mines. I found it particularly useful for deciphering runes.")
                elif (not FundorHasMoonstone and FundorHasRunepaper and current_room.items.find('runepaper')):
                    say("These runes can only be read in the moonlight or by looking through something that has the same magic.")
                elif (FundorHasMoonstone and current_room.items.find('moonstone') and FundorHasRunepaper and current_room.items.find('runepaper'):
                    say("Ah, let's see... what do we have here.... just a moment...")
                    say("...")
                    say("There you go: There is a hidden door within this cave. Its entry can be found at one of the eastern walls.")
                    say("This door is locked and the key is hidden within this cave as well. But the instructions on how to find it are very vague.")
                    say("... something about bottles...")
                    say("I'm sorry, but can't make more sense of it.")
                    global GotLocationOfKey
                    GotLocationOfKey = True
                    if bool(inventory.find('bottle')):
                        global LocalisedKey
                        LocalisedKey = True
                    global GotLocationOfDoor
                    GotLocationOfDoor = True
                else:
                    say("Fúndor is humming quietly...")
            if pers == Nadihm:
                global CountVisitsToNadihm
                CountVisitsToNadihm = CountVisitsToNadihm + 1
                if CountVisitsToNadihm == 1:
                    say("1")
                if CountVisitsToNadihm == 2:
                    say("2")
                if CountVisitsToNadihm > 2:
                    say("3")
            if pers == Frain:
                if not LocalisedKey:
                    say("beer!")
                elif not bool(inventory.find('key')):
                    say("Nice, bottle...drink with me!")
                else:
                    say("sleep")
        else: 
            say("%s is not here." % person)
    else:
        say("There is no one to talk to.")
       

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