class Sort:
    def __init__(self, list):
        self.list = list



    def mySsort(list):
        if list:
            return Sort.mySsort([x for x in list if x < list[0]]) +\
                   [x for x in list if x == list[0]] + \
                   Sort.mySsort([x for x in list if x > list[0]])
        return []


    def search(list, x, lo=0, hi=None):
        if hi is None:
            hi = len(list)
        while lo < hi:
            mid = (lo + hi) // 2
            midval = list[mid]
            if midval < x:
                lo = mid + 1
            elif midval > x:
                hi = mid
            else:
                return mid
        return -1