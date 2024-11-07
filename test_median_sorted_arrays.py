from median_sorted_arrays import *

sol = Solution()

def test1():
    assert sol.findMedianSortedArrays([1, 3], [2]) == 2.0

def test2():
    assert sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5