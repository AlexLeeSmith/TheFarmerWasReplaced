import lib_maneuvering
import lib_planting
import lib_sorting
import lib_util
from __builtins__ import *

GRID_SIZE = 10
SKIP_SUNFLOWERS = 10
MIN_PETALS = 10
sunflowers = []


def plant_sunflower():
    lib_planting.try_harvest()
    lib_planting.till_and_water()
    plant(Entities.Sunflower)
    sunflowers.append((measure(), lib_maneuvering.get_cur_pos()))  # Add (number of petals, current position)


def main():
    global sunflowers
    while True:
        lib_maneuvering.bottom_left()
        lib_maneuvering.zig_zag(plant_sunflower, GRID_SIZE, GRID_SIZE, False)
        lib_sorting.heap_sort(sunflowers, lib_util.get_first)
        while len(sunflowers) > SKIP_SUNFLOWERS:
            num_petals, (x_sunflower, y_sunflower) = sunflowers.pop()
            if num_petals < MIN_PETALS:
                break
            lib_maneuvering.goto(x_sunflower, y_sunflower)
            lib_planting.harvest_when_grown()
        sunflowers = []


if __name__ == "__main__":
    main()
