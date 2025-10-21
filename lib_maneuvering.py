import lib_util
from __builtins__ import *

DIRECTIONS = [North, East, South, West]


def get_cur_pos():
    return get_pos_x(), get_pos_y()


def turn_left(direction):
    index = lib_util.index_of(DIRECTIONS, direction)
    if index >= 0:
        return DIRECTIONS[index - 1]
    else:
        return None


def turn_right(direction):
    index = lib_util.index_of(DIRECTIONS, direction)
    if index >= 0:
        return DIRECTIONS[(index + 1) % len(DIRECTIONS)]
    else:
        return None


def goto_x(x_dest, wrap_allowed=True, do=lib_util.do_nothing):
    x_last_dir = None
    x_delta = x_dest - get_pos_x()
    # Check if moving is necessary
    if x_delta != 0:
        x_dist = abs(x_delta)
        x_dist_wrap = (get_world_size()) - x_dist
        # Check if faster not to world wrap
        if x_dist <= x_dist_wrap or not wrap_allowed:
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
            if not move(x_dir):
                break
            x_last_dir = x_dir

    return x_dest == get_pos_x(), x_last_dir


def goto_y(y_dest, wrap_allowed=True, do=lib_util.do_nothing):
    y_last_dir = None
    y_delta = y_dest - get_pos_y()
    # Check if moving is necessary
    if y_delta != 0:
        y_dist = abs(y_delta)
        y_dist_wrap = (get_world_size()) - y_dist
        # Check if faster not to world wrap
        if y_dist <= y_dist_wrap or not wrap_allowed:
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
            if not move(y_dir):
                break
            y_last_dir = y_dir

    return y_dest == get_pos_y(), y_last_dir


def goto(x_dest, y_dest, wrap_allowed=True, do=lib_util.do_nothing):
    x_arrived, x_dir = goto_x(x_dest, wrap_allowed, do)
    y_arrived, y_dir = goto_y(y_dest, wrap_allowed, do)
    if lib_util.non_none(y_dir):
        last_dir = y_dir
    else:
        last_dir = x_dir
    return x_arrived and y_arrived, last_dir


def goto_retry(x_dest, y_dest, wrap_allowed=True, do=lib_util.do_nothing):
    arrived = False
    last_dir = North
    while not arrived and lib_util.non_none(last_dir):
        arrived, last_dir = goto(x_dest, y_dest, wrap_allowed, do)
    return arrived, last_dir


def bottom_left(wrap_allowed=True, do=lib_util.do_nothing):
    return goto(0, 0, wrap_allowed, do)


def zig_zag(do=lib_util.do_nothing, rows=get_world_size(), cols=get_world_size(), last_move=True):
    y_dir = North
    for row in range(rows):
        for _ in range(cols - 1):
            do()
            if lib_util.is_even(row):
                x_dir = East
            else:
                x_dir = West
            if not move(x_dir):
                return False
        do()
        if row != rows - 1 or last_move:
            if not move(y_dir):
                return False

    return True


def zig_zag_wrap(do=lib_util.do_nothing, rows=get_world_size(), cols=get_world_size()):
    if lib_util.is_odd(rows):
        print("Rows must be even but was ", rows)
        return False
    x_start, y_start = get_cur_pos()
    do()
    if not move(East):
        return False
    if not zig_zag(do, rows, cols - 1, False):
        return False
    arrived, _ = goto(x_start, y_start, False, do)
    return arrived
