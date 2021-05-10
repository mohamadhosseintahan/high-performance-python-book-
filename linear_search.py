l = [2,4,3,5,1,2,5,1,2,1,5,7,3,2,8,4,63,2,6,4,3]

def linear_search(needle , array):
    for i , item in enumerate(array):
        if item == needle:
            return i
    return -1

result = linear_search(63, l)
print(result)