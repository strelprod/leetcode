"""Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]

"""

from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        slow_pointer = 0
        fast_pointer = 0
        nums_len = len(nums)
        while fast_pointer < nums_len:
            if nums[fast_pointer] % 2 == 0:
                nums[slow_pointer], nums[fast_pointer] = nums[fast_pointer], nums[slow_pointer]
                slow_pointer += 1
            fast_pointer += 1
        return nums


nums = [3,1,2,4]
result = [2,4,3,1]
Solution().sortArrayByParity(nums)
assert result == nums

nums = [0]
result = [0]
Solution().sortArrayByParity(nums)
assert result == nums