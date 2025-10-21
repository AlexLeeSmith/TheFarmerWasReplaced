import lib_maneuvering
import lib_planting
from __builtins__ import *

SIZE = 32
no_pumpkins = []


def do():
    lib_planting.till_and_water()
    plant(Entities.Pumpkin)


def check_and_append():
    if not can_harvest():
        no_pumpkins.append(lib_maneuvering.get_cur_pos())
        do()


def check_and_remove():
    if can_harvest():
        no_pumpkins.remove(lib_maneuvering.get_cur_pos())
    else:
        do()


def main():
    while True:
        lib_maneuvering.bottom_left()
        lib_maneuvering.zig_zag_wrap(do, SIZE, SIZE)
        lib_maneuvering.zig_zag_wrap(check_and_append, SIZE, SIZE)
        while len(no_pumpkins) > 0:
            for x_dead, y_dead in no_pumpkins:
                lib_maneuvering.goto(x_dead, y_dead)
                check_and_remove()
        harvest()


if __name__ == "__main__":
    main()
