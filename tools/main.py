from random import randint


def make_some(x: int):
    return x ** 3 - x ** 2


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[randint(0, len(arr) - 1)]
    left, middle, right = [], [], []
    for elem in arr:
        if elem < pivot:
            left.append(elem)
        elif elem == pivot:
            middle.append(elem)
        else:
            right.append(elem)
    return quick_sort(left) + middle + quick_sort(right)


def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr) - i):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    print(quick_sort([5, 8, 2, 7, 0, 6, 5, 3]))
    print(bubble_sort([2, 9, 2, 0, 7, -2, -3]))
