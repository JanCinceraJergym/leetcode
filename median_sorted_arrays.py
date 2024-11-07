from lc import *

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        i = len(nums3)//2
        if len(nums3) % 2 == 0:
            return (nums3[i] + nums3[i - 1]) / 2
        return nums3[i]
        