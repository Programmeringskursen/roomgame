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
rat1 = character.Character("Rat", my_house.cellar)

#Items
muddy_shoes = things.Things("Muddy Shoes", "mud", my_house.hallway)
leather_shoes = things.Things("Nice leather shoes", "leather", my_house.hallway)
knitted_hat = things.Things("Green knitted hat", "sweat", my_house.hallway)
trenchcoat = things.Things("Trenchcoat", "musk", my_house.hallway)
cigarettes = things.Things("A pack of cigarettes", "tobacco", trenchcoat)
matchbox = things.Things("Matchbox", "sulfur", trenchcoat)
magical_map = things.Things("Magical Map", "Wonderful", my_house.hallway)

old_books = things.Things("Alot of old books", "old books", my_house.library)
mysterious_diary = things.Things("Mysterious Diary", "old book", my_house.library)
perfume_bottle = things.Things("Luxurious Perfume", "", my_house.master_bedroom)
roses = things.Things("A boquet of roses", "rose", my_house.living_room)
tulips = things.Things("A boquet of tulips", "tulips", my_house.living_room)
soap = things.Things("Soap", "soap", my_house.toilet)
toothpaste = things.Things("Toothpaste", "spearmint", my_house.toilet)
rat_poison = things.Things("Rat poison", "rat poison", my_house.corridor_west)
mouse_trap = things.Things("Mouse trap", "cheese", my_house.corridor_east)
bowl_of_fruit = things.Things("Bowl of fruit", "fresh fruit", my_house.guest_bedroom)

tea = things.Things("A box of tea", "herby", my_house.kitchen)
oregano = things.Things("An oregano plant", "spicy", my_house.kitchen)
knife_stand = things.Things("A knife stand", "woody", my_house.kitchen)
kitchen_knife = things.Things("Kitchen knife", "not much", knife_stand)
butchers_knife = things.Things("Butchers knife", "not much", knife_stand)
filet_knife = things.Things("Filet knife", "fishy", knife_stand)
bread_knife = things.Things("Bread knife", "not much", knife_stand)

secret_key = things.Key("Secret Key", my_house.secret_room, my_house.library)



