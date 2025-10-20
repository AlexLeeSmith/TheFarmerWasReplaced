import lib_maneuvering
import lib_planting
from __builtins__ import *

SIZE = 10


def plant_carrot():
    lib_planting.try_harvest()
    lib_planting.till_and_water()
    plant(Entities.Carrot)


def main():
    while True:
        lib_maneuvering.bottom_left()
        lib_maneuvering.zig_zag(plant_carrot, SIZE, SIZE, False)


if __name__ == "__main__":
    main()
