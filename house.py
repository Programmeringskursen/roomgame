#!/usr/bin/env python
# -*- coding: utf-8 -*-
import room
import character
class House(object):
    "Map of the house" #comment explanation
    
    def __init__(self):
	self.cellar = room.Room("The Cellar", "Rotten")
	self.hallway = room.Room("The Hallway", "Shoes")
	self.casino = room.Room("The Casino", "Martinis")
	self.library = room.Room("The Library", "Old books")
	self.living_room = room.Room("The Living Room", "Flowers")
	self.toilet = room.Room("The Toilet", "Air Freshener")
	self.kitchen = room.Room("The Kitchen", "Tasty soup")
	self.secret_room = room.Room("The Secret Room", "A serious smell")
	self.master_bedroom = room.Room("The Master Bedroom", "Too much perfume")
	self.guest_bedroom = room.Room("The Guest Bedroom", "Lemons")
        self.corridor_west = room.Room("The West Corridor", "Rat poison")
        self.corridor_east = room.Room("The East Corridor", "Cheese")
        
        
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
        self.master_bedroom.north = self.corridor_east
        self.master_bedroom.west = self.casino
	self.library.east = self.casino
        self.library.south = self.guest_bedroom
        self.guest_bedroom.north = self.library
        self.secret_room.north = self.casino
        self.starting_room = self.cellar
    
    # Go through all rooms and make dictionaries.    
    def visit_all_rooms(self, current_room=None, visited_rooms=None, x=0, y=0, extremevalues=None, mapped_coordinates=None):
	if current_room is None:
	    current_room= self.starting_room	
	if extremevalues is None:
	    extremevalues = {"x_min": 0, "y_min": 0, "x_max": 0, "y_max": 0}	
	if mapped_coordinates is None:
	    mapped_coordinates = {}
	if visited_rooms is None:
            visited_rooms = []
        if current_room == False:
            return mapped_coordinates, extremevalues
        if current_room in visited_rooms:
            return mapped_coordinates, extremevalues
	if x>extremevalues["x_max"]:
	    extremevalues["x_max"] = x
	if x<extremevalues["x_min"]: 
	    extremevalues["x_min"] = x
	if y>extremevalues["y_max"]:
	    extremevalues["y_max"] = y
	if y<extremevalues["y_min"]:
	    extremevalues["y_min"] = y
	    return mapped_coordinates, extremevalues
	else:
	    if x  not in mapped_coordinates:
		mapped_coordinates[x] = {}
	    mapped_coordinates[x][y] = current_room
	    visited_rooms.append(current_room)

	self.visit_all_rooms(current_room.north, visited_rooms, x=x, y=y-1, extremevalues=extremevalues, mapped_coordinates=mapped_coordinates) #kolla om det finns ett rum north om tex. the cellar och skicka in det i visit_all_rooms. Om det ej finns så är det false och då returnar den
        self.visit_all_rooms(current_room.south, visited_rooms, x=x, y=y+1, extremevalues=extremevalues, mapped_coordinates=mapped_coordinates)
        self.visit_all_rooms(current_room.east, visited_rooms, x=x+1, y=y, extremevalues=extremevalues, mapped_coordinates=mapped_coordinates)
        self.visit_all_rooms(current_room.west, visited_rooms, x=x-1, y=y, extremevalues=extremevalues, mapped_coordinates=mapped_coordinates)
        
        return mapped_coordinates, extremevalues

    def pad_name(self, name):
	name=name[4:] #remove "The " from name
	name=name[:16] 
	missing = 16-len(name)
	return name+" "*missing

    #Make the dictionaries from visit_all_rooms into one long string.
    def draw_map(self):
	mapped_coordinates, extremevalues = self.visit_all_rooms()
	map_height = extremevalues["y_max"]-extremevalues["y_min"]+1
	map_width = extremevalues["x_max"]-extremevalues["x_max"]+1
	string = "|"+"_"*76+"\n|"
	for y in range(extremevalues["y_min"], extremevalues["y_max"]+1):
	    string2 = ""
	    for x in range(extremevalues["x_min"], extremevalues["x_max"]+1):
		if x not in mapped_coordinates:
                    name = ""
		    string2 = string2 + "_"*19
		    room = None
		elif y not in mapped_coordinates[x]:
                    name = ""
		    room = None		
		else:
                    name = mapped_coordinates[x][y].name
		    room = mapped_coordinates[x][y]
		string = string + self.pad_name(name) + self.horizontal_door_check(room)
		string2 = string2 + self.vertical_door_check(room)
	    string = string +"\n|" + string2 + "\n|"
	return string

    def horizontal_door_check(self, room):
	if room == None:
	    return " | "
	elif room.east != False:
	    return " > "
	else:
	    return " | "

    def vertical_door_check(self, room):
	string = "_"*9
	if room == None:
	    return string+"_"+string
	elif room.south != False:
	    return string+"/"+string
	else:
	    return string+"_"+string
	
