import math
import random
from inspect import isfunction


def quick_sort(array: list, key_func=lambda x: x) -> list:
    pass


def shell_sort(array: list, key_func=lambda x: x) -> list:
    if key_func is not None:
        assert isfunction(key_func)

    if len(array) < 1:
        return array

    if len(array) == 2:
        return array if array[0] < array[1] else [array[1], array[0]]

    # 1 3 5 8 13 22 etc...
    max_step, gap, steps = math.floor(len(array) / 3), math.inf, [1, 3]
    while True:
        if 0 <= max_step - steps[-1] < gap:
            gap = max_step - steps[-1]
        else:
            break
        steps.append(steps[-1] * 2 - len(steps) + 1)

    for step in reversed(steps[:-1]):
        for pos in range(step, len(array), step):
            insert_item = array[pos]
            idx = pos - step
            while key_func(array[idx]) > key_func(insert_item) and idx >= 0:
                array[idx + step] = array[idx]
                idx -= step
            array[idx + step] = insert_item
    return array


def insertion_sort(array: list, key_func=lambda x: x) -> list:
    """
        best:O(N) avg:O(N^2) worst:O(N^2)
    """
    if key_func is not None:
        assert isfunction(key_func)

    for pos in range(1, len(array)):
        insert_item = array[pos]
        idx = pos-1
        while key_func(array[idx]) > key_func(insert_item) and idx >= 0:
            array[idx+1] = array[idx]
            idx -= 1
        array[idx+1] = insert_item
    return array


def bubble_sort(array: list, key_func=lambda x: x) -> list:
    """
        best:O(N) avg:O(N^2) worst:O(N^2)
    """
    if key_func is not None:
        assert isfunction(key_func)

    for pos in range(0, len(array)):
        for idx in range(0, len(array)-pos-1):
            if key_func(array[idx]) > key_func(array[idx+1]):
                array[idx], array[idx+1] = array[idx+1], array[idx]
    return array


def selection_sort(array: list, key_func=lambda x: x) -> list:
    """
        best:O(N) avg:O(N^2) worst:O(N^2)
    """
    if key_func is not None:
        assert isfunction(key_func)

    for pos in range(0, len(array)):
        min_item_idx = pos
        for idx in range(pos, len(array)):
            if key_func(array[idx]) < key_func(array[min_item_idx]):
                min_item_idx = idx

        array[pos], array[min_item_idx] = array[min_item_idx], array[pos]
    return array


def _assert_sorted(origin_array: list, array: list, key_func=lambda x: x) -> bool:
    key_array = [key_func(item) for item in array]
    previous = None
    has_sorted = True
    for key in key_array:
        if previous is None:
            previous = key
            continue
        if key < previous:
            has_sorted = False
            break
        else:
            previous = key

    return sorted(origin_array) == array and has_sorted


if __name__ == '__main__':
    unsort_array = [random.randrange(-99, 99) for _ in range(40)]
    sorted(unsort_array)
    print(unsort_array)
    copy_array = unsort_array.copy()
    sorted_array = shell_sort(unsort_array)
    print(sorted_array)
    print(_assert_sorted(copy_array, sorted_array))

