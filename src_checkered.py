import lib_maneuvering
import lib_planting
from __builtins__ import *

SIZE = 10
PLANT_1 = Entities.Tree
PLANT_2 = Entities.Carrot


def main():
    lib_maneuvering.bottom_left()
    while True:
        lib_maneuvering.zig_zag_wrap(lib_planting.checkered(PLANT_1, PLANT_2),
                                     SIZE, SIZE)


if __name__ == "__main__":
    main()
