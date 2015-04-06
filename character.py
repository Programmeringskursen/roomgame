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
	self.scope = self
	self.keychain = []
	
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
	if type(obj) == things.Things:	
	    if len(self.content)>10:
	        return "You can't carry anymore."
	    if obj in self.scope.content:
	        self.scope.content.remove(obj)
	        self.content.append(obj)
		return "You picked up "+obj.name+"."
	    if obj not in self.position.content:
	        return "THERE IS NO SUCH THING! ARE YOU HALLUCINATING?"
	    else:
	        self.position.content.remove(obj)
	        self.content.append(obj)
	    return "You picked up "+obj.name+"."
	
	if type(obj) == things.Key:
	    if obj in self.scope.content:
	        self.scope.content.remove(obj)
	        self.keychain.append(obj)
		return "You added "+obj.name+" to you keychain."
	    if obj not in self.position.content:
	        return "THERE IS NO SUCH THING! ARE YOU HALLUCINATING?"
	    else:
	        self.position.content.remove(obj)
	        self.keychain.append(obj)
	    return "You added "+obj.name+" to your keychain."
	
	else:
	    return "This is not something you can pick up."

    def drop(self, obj):
	"Drop things in the characters current room."
	if not obj in self.content:
	    return "You can not drop what you do not have."
	self.content.remove(obj)
	self.position.content.append(obj)
	return "You dropped "+str(obj)+"."

    def look_inside(self, obj): #look inside objects. makes it possible to pick up things from inside objects. eg a single cigarette from inside a package.
	things = []	
	if obj not in self.position.content or self.content or self.scope.content:
	    return "THERE IS NO SUCH THING! ARE YOU HALLUCINATING?"
	else:
	    self.scope = obj
	    for Things in obj.content:
                things.append(str(Things))
	    return "You see "+" and ".join(things)+"."

    def move(self, direction):
	self.scope = self
        if direction=="north":
            if self.position.north == False:
                return "You can't, there is no door here."
            else:
		return self.check_lock(self.position.north)

        elif direction=="south":
            if self.position.south == False:
                return "You can't, there is no door here."
            else:
                return self.check_lock(self.position.south)

        elif direction=="west":
            if self.position.west == False:
                return "You can't, there is no door here."
            else:
                return self.check_lock(self.position.west)

        elif direction=="east":
            if self.position.east == False:
                return "You can't, there is no door here."
            else:
                return self.check_lock(self.position.east)

    def check_lock(self, room):
	access = False	
	if room.lock == False:
	    self.position = room
	    return "You enter the "+self.position.name+"."
	else:
	    for Key in self.keychain:
		if Key.unlock == room:
		    access = True
	    if access == True:
		self.position = room	
	        return "You unlock the door and enter the "+self.position.name+"."
	    else:
		return "You can't, it's locked."
	    

    def __str__(self):
        inventory = []
        for obj in self.content:
            inventory.append(str(obj))
        return "You are in "+self.position.name+". "+"In your inventory there are " + " and ".join(inventory)+"."
