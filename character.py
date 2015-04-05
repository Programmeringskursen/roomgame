#!/usr/bin/env python
# -*- coding: utf-8 -*-
import room
import house
import things
class Character(object):

    def __init__(self, name, position):
	self.content = []
	self.name = name
	self.position = position
	self.scope = None
	
    def choose_player(self, name):
	if position != self.hallway:
	    return "You must be in the hallway to change player"
	if name=="Elin":
	    return "You are playing as Elin"
	if name=="Murneh":
	    return "You are playing as Murneh"
	return "You must choose either Murneh or Elin"
    

    def pick_up(self, obj):
	"Pick up things from the room the character is in."
	if not obj in self.position.content:
	    return "THERE IS NO SUCH THING! ARE YOU HALLUCINATING?"
	self.position.content.remove(obj)
	self.content.append(obj)
	return "You picked up "+obj.name+"."

    def drop(self, obj):
	"Drop things in the characters current room."
	if not obj in self.content:
	    return "You can not drop what you do not have."
	self.content.remove(obj)
	self.position.content.append(obj)
	return "You dropped "+str(obj)+"."

    def look_inside(self, obj): #look inside objects. makes it possible to pick up things from inside objects. eg a single cigarette from inside a package.
	if obj not in self.position.content or self.content or self.scope:
	    return "THERE IS NO SUCH THING! ARE YOU HALLUCINATING?"
	self.scope = obj
	return "You see "+" and ".join(obj.content)+"."

    def move(self, direction):
	self.scope = None
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
