import random
from inspect import isfunction


def quick_sort(array: list, key_func=lambda x: x) -> list:
    pass


def shell_sort(array: list, key_func=lambda x: x) -> list:

    pass


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


def _assert_sorted(array: list, key_func=lambda x: x) -> bool:
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

    return has_sorted


if __name__ == '__main__':
    unsort_array = [random.randrange(-9, 9) for _ in range(10)]
    sorted(unsort_array)
    print(unsort_array)
    sorted_array = bubble_sort(unsort_array)
    print(sorted_array)
    print(_assert_sorted(sorted_array))

