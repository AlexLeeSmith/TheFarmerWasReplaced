import lib_maneuvering
import lib_planting


def do():
    lib_planting.try_harvest()
    lib_planting.untill_and_water()


def main():
    lib_maneuvering.bottom_left()
    while True:
        lib_maneuvering.zig_zag(do)


if __name__ == "__main__":
    main()
