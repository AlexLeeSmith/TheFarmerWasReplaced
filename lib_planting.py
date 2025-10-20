import lib_util
from __builtins__ import *

UNTILLED = {Entities.Grass, Entities.Bush}


def try_harvest():
    if can_harvest():
        harvest()


def harvest_when_grown():
    while not can_harvest():
        pass
    harvest()


def water(threshold=0.0):
    while get_water() < threshold:
        use_item(Items.Water)


def till_and_water(threshold=0.0):
    if get_ground_type() != Grounds.Soil:
        till()
    water(threshold)


def untill_and_water(threshold=0.0):
    if get_ground_type() != Grounds.Grassland:
        till()
    water(threshold)


def checkered(plant_1, plant_2=Entities.Grass, water_threshold_1=0.0, water_threshold_2=0.0):
    def f():
        try_harvest()
        if lib_util.is_even(get_pos_x() + get_pos_y()):
            if plant_1 in UNTILLED:
                untill_and_water(water_threshold_1)
            else:
                till_and_water(water_threshold_1)
            plant(plant_1)
        else:
            if plant_2 in UNTILLED:
                untill_and_water(water_threshold_2)
            else:
                till_and_water(water_threshold_2)
            plant(plant_2)

    return f
