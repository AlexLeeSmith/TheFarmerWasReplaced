import lib_maneuvering
import lib_planting
from __builtins__ import *

SIZE = 10


def main():
    while True:
        lib_maneuvering.bottom_left()
        lib_maneuvering.zig_zag(lib_planting.checkered(Entities.Tree, Entities.Carrot),
                                SIZE, SIZE, False)


if __name__ == "__main__":
    main()
