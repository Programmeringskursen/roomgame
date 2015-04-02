#!/usr/bin/env python
# -*- coding: utf-8 -*-
#åäö i kommentarer^
import house
import room
import character
import things


my_house=house.House()
player = character.Character("Murneh", my_house.hallway)
magical_map = things.Things("Magical Map", "Wonderful", my_house.hallway)
