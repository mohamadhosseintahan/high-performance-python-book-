l = [2, 4, 3, 5, 1, 2, 5, 1, 2, 1, 5, 7, 2, 8, 1, 4, 63, 2, 6, 4, 3]
l.sort()


def binary_search(needle, haystack):
    imin, imax = 0, len(haystack)
    while True:
        if imin > imax:
            return -1
        midpoint = (imin + imax) // 2
        if haystack[midpoint] > needle:
            imax = midpoint
        elif haystack[midpoint] < needle:
            imin = midpoint + 1
        else:
            return midpoint


result = binary_search(63, l)
print(result)
