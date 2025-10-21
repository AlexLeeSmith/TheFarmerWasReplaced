def do_nothing():
    pass


def is_none(x):
    return None == x


def non_none(x):
    return not is_none(x)


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return not is_even(n)


def get_first(collection):
    return collection[0]


def index_of(collection, it):
    for i in range(len(collection)):
        if collection[i] == it:
            return i
    return -1


def identity(x):
    return x


def less_than(a, b):
    return a < b


def greater_than(a, b):
    return a > b
