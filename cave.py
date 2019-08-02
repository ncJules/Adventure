from adventurelib_with_characters import *


""" adventure specific settings """

"""define the items available and where to find them"""
Room.items = Bag()

axe = Item('axe', 'axe')
key = Item('key', 'key')
letter = Item('letter', 'a letter from Dàin')
moonstone = Item('moonstone', 'moonstone')
runepaper = Item('runepaper', 'runepaper')
winebottle = Item('bottle', 'bottle')




"""define characters"""
Room.characters = Group()

Nadihm = Character('Nadihm', 'Nadihm')
Fundor = Character('Fundor', 'Fundor')
Frain = Character('Frain', 'Frain')

"""define the rooms available, their descriptions, contained items and connections"""

hall = Room("""You are in a hall""")
hall.characters = Group({Fundor,})

living = hall.north = Room("""You are in a living room""")
living.characters = Group({Nadihm,})

supplyI = hall.east = Room("""You are in supply room containing tools and stuff""")

dining = living.east = Room("""You are in the dining room""")

kitchen = dining.north = Room("""You are in the kitchen""")
kitchen.characters = Group({Frain,})

supplyII = kitchen.east = Room("""You are in a supply room with food and drinks.""")

sleeping = kitchen.west = Room("""You are small room containing three sleeping arrangements""")
sleeping.items = Bag({axe,})

treasure = Room("""You have finally found the treaure room. Yay!""")





""" init """

current_room = hall

inventory = Bag({letter,})

UsedSteps = 0