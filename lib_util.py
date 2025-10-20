def do_nothing():
    pass


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return not is_even(n)


def get_first(collection):
    return collection[0]


def identity(x):
    return x


def less_than(a, b):
    return a < b


def greater_than(a, b):
    return a > b
