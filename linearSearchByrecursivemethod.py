#LinearSearchByRecursiveMethod
def linearSearchByRecursive(l,target):
    return linearSearchByRecursive2(l,0,target)

def linearSearchByRecursive2(l,index,target):
    if l == []:
        return -1
    if l[0] == target:
        return index 
    return linearSearchByRecursive2(l[1:], index+1, target)

print(linearSearchByRecursive([4,5,65,8,2,1,7],8))

print(linearSearchByRecursive([4,5,65,8,2,1,7],88))
