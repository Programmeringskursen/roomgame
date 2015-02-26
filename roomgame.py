#!/usr/bin/env python
class Room(object):
    "Our little game"
    
    def __init__(self, name):
        self.content = []
        self.name = name
	self.north = False
	self.south = False
	self.west = False
	self.east = False
        
    def place_here(self, obj):
        self.content.append(obj)
        
    def remove(self, obj):
        "Ta bort!!"
        self.content.remove(obj)
        
    def __str__(self):
        things = []
        for obj in self.content:
            things.append(str(obj))
        return "In " + self.name + " there are " + " and ".join(things)
    
    
    
class House(object):
    "Map of the house" #comment explanation
    
    def __init__(self):
	self.cellar = Room("The Cellar")
	self.hallway = Room("The Hallway")
	self.casino = Room("The Casino")
	self.library = Room("The Library")
	self.living_room = Room("The Living Room")
	self.toilet = Room("The Toilet")
	self.kitchen = Room("The Kitchen")
	self.secret_room = Room("The Secret Room")
	self.master_bedroom = Room("The Master Bedroom")
	self.guest_bedroom = Room("The Guest Bedroom")
	

class Character(object):

    def __init__(self, name, position):
	self.content = []
	self.name = name
	self.position = position

    def pick_up(self, obj):
	"Pick up things the character is in."
	self.position.content.remove(obj)
	self.content.append(obj)

    def drop(self, obj):
	"Drop things in the characters current room."
	self.content.remove(obj)
	self.position.content.append(obj)

    def movenorth(self):
	if self.position.north == False:
	  return "You can't, there is no door here."
	else:
	  self.position = self.position.north
	  return "You enter the "+self.position.name+"."

    def movesouth(self):
	if self.position.south == False:
	  return "You can't, there is no door here."
	else:
	  self.position = self.position.south
	  return "You enter the "+self.position.name+"."

    def movewest(self):
	if self.position.west == False:
	  return "You can't, there is no door here."
	else:
	  self.position = self.position.west
	  return "You enter the "+self.position.name+"."

    def moveeast(self):
	if self.position.east == False:
	  return "You can't, there is no door here."
	else:
	  self.position = self.position.east
	  return "You enter the "+self.position.name+"."

    def __str__(self):
        inventory = []
        for obj in self.content:
            inventory.append(str(obj))
        return "You are in "+self.position.name+". "+"In your inventory there are " + " and ".join(inventory)+"."


# The house and the connection between rooms.
lvl1 = House()

lvl1.hallway.south = lvl1.toilet
lvl1.hallway.west = lvl1.cellar
lvl1.hallway.east = lvl1.living_room

lvl1.cellar.east = lvl1.hallway

lvl1.toilet.north = lvl1.hallway

lvl1.living_room.south = lvl1.casino
lvl1.living_room.west = lvl1.hallway
lvl1.living_room.east = lvl1.kitchen

lvl1.kitchen.south = lvl1.master_bedroom
lvl1.kitchen.west = lvl1.living_room

lvl1.casino.north = lvl1.living_room
lvl1.casino.south = lvl1.secret_room
lvl1.casino.west = lvl1.library
lvl1.casino.east = lvl1.master_bedroom

lvl1.master_bedroom.north = lvl1.kitchen
lvl1.master_bedroom.west = lvl1.casino

lvl1.library.south = lvl1.guest_bedroom

lvl1.guest_bedroom.north = lvl1.library

lvl1.secret_room.north = lvl1.casino


player = Character("Murneh", lvl1.hallway)

