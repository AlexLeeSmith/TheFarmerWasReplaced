import lib_maneuvering
from __builtins__ import *


def collect_apples():
    clear()
    change_hat(Hats.Dinosaur_Hat)
    last_dir = North
    while True:
        if get_entity_type() == Entities.Apple:
            # Get next apple's position
            x_next_apple, y_next_apple = measure()
            # Harvest current apple
            if not move(last_dir) and not move(lib_maneuvering.turn_left(last_dir)) and not move(
                    lib_maneuvering.turn_right(last_dir)):
                print("Cannot harvest apple!")
                break
        else:
            print("Apple not found!")
            break
        # Move to next apple
        _, last_dir = lib_maneuvering.goto_retry(x_next_apple, y_next_apple, False)


def main():
    while True:
        collect_apples()


if __name__ == "__main__":
    main()
