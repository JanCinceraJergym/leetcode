from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while True:
            print(f"{left}, {right}")
            if left == right:
                continue
            if nums[left] + nums[right] == target:
                return [left, right]
            
            if nums[left] + nums[right] > target:
                if nums[left+1] < nums[left]:
                    left += 1
                elif nums[right-1] < nums[right]:
                    right -= 1
            else:
                if nums[left+1] > nums[left]:
                    left += 1
                elif nums[right-1] > nums[right]:
                    right -= 1
