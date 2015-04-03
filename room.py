#!/usr/bin/env python
# -*- coding: utf-8 -*-
import house
import character
import things
class Room(object):
    "Our little game"
    
    def __init__(self, name, smell):
        self.content = []
        self.name = name
	self.smell = smell
	self.north = False
	self.south = False
	self.west = False
	self.east = False
    
    def stink(self):
	smells = []
	for obj in self.content:
	    smells.append(str(obj.smell))
	return "It reeks of a mixture of "+" and ".join(smells)+"."	    	
    
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
    
    def __repr__(self):
	return self.name
