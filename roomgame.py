#!/usr/bin/env python
# -*- coding: utf-8 -*-
#åäö i kommentarer^
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
        self.corridor_west = Room("The West Corridor")
        self.corridor_east = Room("The East Corridor")
        
        
        # The house and the connection between rooms.
	self.hallway.south = self.toilet
        self.hallway.west = self.cellar
        self.hallway.east = self.living_room
        self.cellar.east = self.hallway
        self.toilet.north = self.hallway
        self.living_room.south = self.corridor_west
        self.living_room.west = self.hallway
        self.living_room.east = self.kitchen
        self.kitchen.south = self.corridor_east
        self.kitchen.west = self.living_room
	self.corridor_west.north = self.living_room
	self.corridor_west.south = self.casino
	self.corridor_east.north = self.kitchen
	self.corridor_east.south = self.master_bedroom
        self.casino.north = self.corridor_west
        self.casino.south = self.secret_room
        self.casino.west = self.library
        self.casino.east = self.master_bedroom
        self.master_bedroom.north = self.kitchen
        self.master_bedroom.west = self.casino
	self.library.east = self.casino
        self.library.south = self.guest_bedroom
        self.guest_bedroom.north = self.library
        self.secret_room.north = self.casino
	self.map = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
        
        
    def visit_all_rooms(self, current_room, visited_rooms=None, x=0, y=0, extremevalues=None):
        if visited_rooms is None:
            visited_rooms = []
        if extremevalues is None:
           extremevalues = {"x_min": x, "y_min": y, "x_max": x, "y_max": y}
        else:
            if y>y_max: extremevalues["y_max"]=y
            if x>x_max: extremevalues["x_max"]=x
            if y>y_min: extremevalues["y_min"]=y
            if x>x_min: extremevalues["x_min"]=x
            
            
        if current_room == False:
            return
        if current_room in visited_rooms:
            return None
        
        print current_room.name, ":" , "(",x, ",",y,")", extremevalues
        visited_rooms.append(current_room)
        
            
        self.visit_all_rooms(current_room.north, visited_rooms, x=x, y=y+1) #kolla om det finns ett rum north om tex. the cellar och skicka in det i visit_all_rooms. Om det ej finns så är det false och då returnar den
        self.visit_all_rooms(current_room.south, visited_rooms, x=x, y=y-1)
        self.visit_all_rooms(current_room.east, visited_rooms, x=x+1, y=y)
        self.visit_all_rooms(current_room.west, visited_rooms, x=x-1, y=y)
        
        
       
     
    
        
        

class Character(object):

    def __init__(self, name, position):
	self.content = []
	self.name = name
	self.position = position

    def pick_up(self, obj):
	"Pick up things from the room the character is in."
	if not obj in self.position.content:
	    return "THERE IS NO SUCH THING! ARE YOU HALLUCINATING?"
	self.position.content.remove(obj)
	self.content.append(obj)
	return "You picked up "+str(obj)+"."

    def drop(self, obj):
	"Drop things in the characters current room."
	if not obj in self.content:
	    return "You can not drop what you do not have."
	self.content.remove(obj)
	self.position.content.append(obj)
	return "You dropped "+str(obj)+"."



    def move(self, direction):
        if direction=="north":
            if self.position.north == False:
                return "You can't, there is no door here."
            else:
	        self.position = self.position.north
                return "You enter the "+self.position.name+"."
        elif direction=="south":
        
            if self.position.south == False:
                return "You can't, there is no door here."
            else:
                self.position = self.position.south
                return "You enter the "+self.position.name+"."
        elif direction=="west":
            
            if self.position.west == False:
                return "You can't, there is no door here."
            else:
                self.position = self.position.west
                return "You enter the "+self.position.name+"."
        elif direction=="east":

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





my_house=House()
your_house=House()
player = Character("Murneh", my_house.hallway)


