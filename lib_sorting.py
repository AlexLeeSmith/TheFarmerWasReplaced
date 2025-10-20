import lib_util
from __builtins__ import *


def _percolate_down(collection, size, root_index, key, compare):
    largest_index = root_index  # Initialize largest as root
    left_index = 2 * root_index + 1
    right_index = 2 * root_index + 2

    # Check if left exists and how it compares to largest
    if left_index < size and compare(key(collection[left_index]), key(collection[largest_index])):
        largest_index = left_index

    # Check if right exists and how it compares to largest
    if right_index < size and compare(key(collection[right_index]), key(collection[largest_index])):
        largest_index = right_index

    # If largest is not root, swap and percolate the subtree
    if largest_index != root_index:
        collection[root_index], collection[largest_index] = collection[largest_index], collection[root_index]
        _percolate_down(collection, size, largest_index, key, compare)


def _build_heap(collection, key, compare):
    size = len(collection)
    # Start from the last non-leaf node and go up to the root
    for i in range(size // 2 - 1, -1, -1):
        _percolate_down(collection, size, i, key, compare)


def _sort_heap(collection, key, compare):
    size = len(collection)
    # Repeatedly swap last with root and percolate the reduced tree
    for i in range(size - 1, 0, -1):
        collection[i], collection[0] = collection[0], collection[i]
        _percolate_down(collection, i, 0, key, compare)


def heap_sort(collection, key=lib_util.identity, reverse=False):
    compare = lib_util.greater_than
    if reverse:
        compare = lib_util.less_than
    _build_heap(collection, key, compare)
    _sort_heap(collection, key, compare)
