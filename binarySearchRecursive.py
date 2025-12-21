def binarySearchRecursive(array, target):
    return binarySearchRecursive2(array, 0, len(array) - 1, target)

def binarySearchRecursive2(array, l, r, target):
    if l > r:
        return -1

    mid = l + (r - l) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binarySearchRecursive2(array, l, mid - 1, target)
    else:
        return binarySearchRecursive2(array, mid + 1, r, target)

print(binarySearchRecursive([2, 3, 4, 10, 40], 10))
