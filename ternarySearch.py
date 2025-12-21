def ternarySearchAlgorithm(array, target):
    return ternarySearch(array, 0, len(array) - 1, target)


def ternarySearch(array, l, r, target):
    if l > r:
        return -1

    mid1 = l + (r - l) // 3
    mid2 = r - (r - l) // 3

    if target == array[mid1]:
        return mid1
    if target == array[mid2]:
        return mid2

    if target < array[mid1]:
        return ternarySearch(array, l, mid1 - 1, target)
    elif target > array[mid2]:
        return ternarySearch(array, mid2 + 1, r, target)
    else:
        # the target is between mid1 and mid2
        return ternarySearch(array, mid1 + 1, mid2 - 1, target)


array = [10, 20, 30, 40, 50, 60, 70, 80]

print(ternarySearchAlgorithm(array, 10))   # Output: 0
print(ternarySearchAlgorithm(array, 75))   # Output: -1

