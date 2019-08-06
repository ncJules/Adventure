from adventurelib_with_characters import *


""" adventure specific settings """

"""define the items available and where to find them"""
Room.items = Bag()

axe = Item('axe', 'axe')
key = Item('key', 'key')
letter = Item('letter', 'a letter from Dàin')
moonstone = Item('moonstone', 'moonstone')
runepaper = Item('runepaper', 'runepaper')
winebottle = Item('winebottle', 'bottle')
longbow = Item('longbow','bow')
arrows = Item('arrows', 'arrows')
ham = Item('ham', 'ham')
spoon = Item('spoon', 'spoon')
ring = Item('ring with elven writing', 'ring')
beads = Item('some golden beads', 'beads')
gems = Item('some beautiful gemstones', 'gemstones', 'gems')
sword = Item('very rusty sword', 'sword')


"""define characters"""
Room.characters = Group()

Nadihm = Character('Nadihm', 'Nadihm')
Fundor = Character('Fundor', 'Fundor')
Frain = Character('Frain', 'Frain')


"""define the rooms available, their descriptions, contained items, people and connections"""

hall = Room("""You are in a hall""")
hall.characters = Group({Fundor,})
hall.items = Bag({longbow,})

living = hall.north = Room("""You are in room which seems to be used as living room. But you don't care too much for the interior as you your nephew fletching some arrows... """)
living.characters = Group({Nadihm,})
living.items = Bag({arrows,})

supplyI = hall.east = Room("""You are in supply room containing tools and other useful stuff.""")
supplyI.items = Bag({axe,})

dining = living.east = Room("""You are in the dining room""")
dining.items = Bag({ring, moonstone, beads, gems})

kitchen = dining.north = Room("""You are in the kitchen""")
kitchen.characters = Group({Frain,})
kitchen.items = Bag({spoon,})

supplyII = kitchen.east = Room("""You are in a supply room with food and drinks.""")
supplyII.items = Bag({winebottle,ham})

sleeping = kitchen.west = Room("""You are small room containing three sleeping arrangements""")
sleeping.items = Bag({runepaper,})

treasure = Room("""You have finally found the treaure room. Yay!""")
treasure.items = Bag({sword,})




""" init """

current_room = hall

inventory = Bag({letter,})

UsedSteps = 0