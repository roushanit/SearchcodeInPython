#linearSearch by iterative method

def linearsearch(l,target):
    for i in range(0,len(l)):
        if l[i] == target:
            return i
    return -1

print(linearsearch([4,5,65,8,2,1,7],88))

