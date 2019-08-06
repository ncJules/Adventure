from adventurelib_with_characters import *


""" adventure specific settings """

"""define the items available and where to find them"""
Room.items = Bag()

axe = Item('an axe', 'axe')
key = Item('a key', 'key')
letter = Item('a letter from Dàin', 'letter')
moonstone = Item('a moonstone', 'moonstone')
runepaper = Item('a runepaper', 'runepaper')
winebottle = Item('a winebottle', 'bottle')
longbow = Item('a longbow','bow')
arrows = Item('some arrows', 'arrows')
ham = Item('a huge, good-looking ham', 'ham')
spoon = Item('a spoon', 'spoon')
ring = Item('a ring with elven writing', 'ring')
beads = Item('some golden beads', 'beads')
gems = Item('some beautiful gemstones', 'gemstones', 'gems')
sword = Item('a very rusty sword', 'sword')


"""define characters"""
Room.characters = Group()

Nadihm = Character('Nadihm', 'Nadihm')
Fundor = Character('Fundor', 'Fundor')
Frain = Character('Frain', 'Frain')


"""define the rooms available, their descriptions, contained items, people and connections"""

hall = Room("""You are in a hall.""")
hall.characters = Group({Fundor,})
hall.items = Bag({longbow,})

living = hall.north = Room("""You are in room which seems to be used as living room. """)
living.characters = Group({Nadihm,})
living.items = Bag({arrows,})

supplyI = hall.east = Room("""You are in supply room containing tools and other useful stuff.""")
supplyI.items = Bag({axe,})

dining = living.east = Room("""You are in the dining room. This never seems to have been used, but you see a big bowl with some small treasures standing on a big cupboard at the east wall.""")
dining.items = Bag({ring, moonstone, beads, gems})

kitchen = dining.north = Room("""You are in the kitchen.""")
kitchen.characters = Group({Frain,})
kitchen.items = Bag({spoon,})

supplyII = kitchen.east = Room("""You are in a supply room with food and drinks. Most things in here you would need to be very desperate to eat, but surely something useful can be found here.""")
supplyII.items = Bag({winebottle,ham})

sleeping = kitchen.west = Room("""You are small room containing three sleeping arrangements. You don't want to go your fellow dwarfs personal belongings, but something seems to be placed there just for you...""")
sleeping.items = Bag({runepaper,})

treasure = Room("""You have finally found the treasure room. But unfortunately it has not been used for a very long time - there's not much to be found.""")
treasure.items = Bag({sword,})




""" init """

current_room = hall

inventory = Bag({letter,})

UsedSteps = 0