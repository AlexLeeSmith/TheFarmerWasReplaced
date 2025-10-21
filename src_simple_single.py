import lib_maneuvering
import lib_planting
from __builtins__ import *

SIZE = 10
PLANT = Entities.Carrot
WATER_THRESHOLD = 0.0


def plant_single():
    lib_planting.try_harvest()
    lib_planting.till_water_plant(PLANT, WATER_THRESHOLD)


def main():
    while True:
        lib_maneuvering.bottom_left()
        lib_maneuvering.zig_zag(plant_single, SIZE, SIZE, False)


if __name__ == "__main__":
    main()
