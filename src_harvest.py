import lib_maneuvering
import lib_planting


def do():
    lib_planting.try_harvest()


def main():
    lib_maneuvering.zig_zag(do)


if __name__ == "__main__":
    main()
