#!/usr/bin/env python
class Room(object):
    "Our little game"
    
    def __init__(self, name):
        self.content = []
        self.name = name
        
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
    
    def __init__(self, name):
       self.cellar = Room("The Cellar")
       self.hallway = Room("The Hallway")
       self.casino = Room("The Casino")
       self.library = Room("The Library")
       self.living_room = Room("The Living Room")
       self.toilet = Room("The Toilet")
       self.kitchen = Room("The Kitchen")
       self.secret_room = Room("The Secret Room")
       self.name = name



