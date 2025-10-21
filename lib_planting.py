import lib_util
from __builtins__ import *

UNTILLED = {Entities.Grass, Entities.Bush}


def try_harvest():
    if can_harvest():
        harvest()
        return True
    return False


def harvest_when_grown():
    while not can_harvest():
        pass
    harvest()


def water(water_threshold=0.0):
    while get_water() < water_threshold:
        use_item(Items.Water)


def till_and_water(water_threshold=0.0):
    if get_ground_type() != Grounds.Soil:
        till()
    water(water_threshold)


def untill_and_water(water_threshold=0.0):
    if get_ground_type() != Grounds.Grassland:
        till()
    water(water_threshold)


def till_water_plant(p, water_threshold=0.0):
    if p in UNTILLED:
        untill_and_water(water_threshold)
    else:
        till_and_water(water_threshold)
    plant(p)


def simple(p, water_threshold=0.0):
    def f():
        try_harvest()
        till_water_plant(p, water_threshold)

    return f


def checkered(plant_1, plant_2=Entities.Grass, water_threshold_1=0.0, water_threshold_2=0.0):
    def f():
        try_harvest()
        if lib_util.is_even(get_pos_x() + get_pos_y()):
            till_water_plant(plant_1, water_threshold_1)
        else:
            till_water_plant(plant_2, water_threshold_2)

    return f
