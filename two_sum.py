from lc import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i::]):
                if i == j+i:
                    continue
                if a + b == target:
                    return [i, j+i]