"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if sum(nums) == 0:
            return
        slow_pointer = 0
        fast_pointer = 0
        nums_len = len(nums)
        while fast_pointer < nums_len:
            if nums[fast_pointer] != 0:
                if fast_pointer != slow_pointer:
                    nums[slow_pointer], nums[fast_pointer] = nums[fast_pointer], nums[slow_pointer]
                slow_pointer += 1
            fast_pointer += 1

nums = [0,1,0,3,12]
result = [1,3,12,0,0]
Solution().moveZeroes(nums)
assert result == nums

nums = [0]
result = [0]
Solution().moveZeroes(nums)
assert result == nums