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
    
    def __init__(self):
       self.rooms = [Room("The Cellar"),
                     Room("The Hallway"),
                     Room("The Casino"),
                     Room("The Library"),
                     Room("The Living Room"),
                     Room("The Toilet"),
                     Room("The Kitchen"),
                     Room("The Secret Room")]
        
    
 


