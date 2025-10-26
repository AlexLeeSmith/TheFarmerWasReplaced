import lib_maneuvering
from __builtins__ import *


def collect_apples():
    clear()
    change_hat(Hats.Dinosaur_Hat)
    while lib_maneuvering.zig_zag_wrap():
        pass


def main():
    # Don't loop because it takes so long for larger worlds
    collect_apples()


if __name__ == "__main__":
    main()
