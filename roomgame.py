#!/usr/bin/env python
# -*- coding: utf-8 -*-
#åäö i kommentarer^
import house
import room
import character
import things

#The house
my_house=house.House()

#Characters
player = character.Character("Murneh", my_house.hallway)
player2 = character.Character("Elin", my_house.hallway) #kan den här också heta player?

#Items
muddy_shoes = things.Things("Muddy Shoes", "mud", my_house.hallway)
leather_shoes = things.Things("Nice leather shoes", "leather", my_house.hallway)
magical_map = things.Things("Magical Map", "Wonderful", my_house.hallway)
old_books = things.Things("Alot of old books", "old books", my_house.library)
perfume_bottle = things.Things("Luxurious Perfume", "strong perfume", my_house.master_bedroom)
roses = things.Things("A boquet of roses", "rose", my_house.living_room)
tulips = things.Things("A boquet of tulips", "tulips", my_house.living_room)


