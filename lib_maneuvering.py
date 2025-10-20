import lib_util
from __builtins__ import *


def get_cur_pos():
    return get_pos_x(), get_pos_y()


def goto_x(x_dest, do=lib_util.do_nothing):
    x_delta = x_dest - get_pos_x()
    # Check if moving is necessary
    if x_delta != 0:
        x_dist = abs(x_delta)
        x_dist_wrap = (get_world_size()) - x_dist
        # Check if faster not to world wrap
        if x_dist <= x_dist_wrap:
            num_moves = x_dist
            x_dir = West
            if x_delta > 0:
                x_dir = East
        else:
            num_moves = x_dist_wrap
            x_dir = East
            if x_delta > 0:
                x_dir = West
        # Do and move
        for _ in range(num_moves):
            do()
            move(x_dir)


def goto_y(y_dest, do=lib_util.do_nothing):
    y_delta = y_dest - get_pos_y()
    # Check if moving is necessary
    if y_delta != 0:
        y_dist = abs(y_delta)
        y_dist_wrap = (get_world_size()) - y_dist
        # Check if faster not to world wrap
        if y_dist <= y_dist_wrap:
            num_moves = y_dist
            y_dir = South
            if y_delta > 0:
                y_dir = North
        else:
            num_moves = y_dist_wrap
            y_dir = North
            if y_delta > 0:
                y_dir = South
        # Do and move
        for _ in range(num_moves):
            do()
            move(y_dir)


def goto(x_dest, y_dest, do=lib_util.do_nothing):
    goto_y(y_dest, do)
    goto_x(x_dest, do)


def bottom_left():
    goto(0, 0)


# Best if rows == cols and isEven
def zig_zag(do, rows=get_world_size(), cols=get_world_size(), last_move=True, reverse=False):
    y_dir = North
    if reverse:
        y_dir = South
    for row in range(rows):
        for col in range(cols):
            do()
            if col == cols - 1:
                pass
            elif lib_util.is_even(row):
                move(East)
            else:
                move(West)
        if row != rows - 1 or last_move:
            move(y_dir)
