def binarySearch(array, target):
    return binarySearch2(array, 0, len(array)-1, target)

def binarySearch2(array, l, r, target):
    while l<= r:
        mid = l + (r-1) // 2

        if array[mid] == target:
            return mid

        elif array[mid] < target:
            l = mid + 1 

        else:
            r = mid -1

    return -1   

print(binarySearch([2,3,5,45,64], 5))                     
