#!/usr/bin/env python
# -*- coding: utf-8 -*-
import character
import house
import room
class Things(object):
    
    def __init__(self, name, smell, position):
        self.content = []
        self.name = name
	self.smell = smell
	position.content.append(self)

    def stink(self):
	return "It smells "+self.smell+"."

    def __str__(self):
	return self.name

    def __repr__(self):
	return self.name
