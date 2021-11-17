"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_set = set()
        for val in nums:
            if val in nums_set:
                nums_set.remove(val)
            else:
                nums_set.add(val)
        return nums_set.pop()


assert 1 == Solution().singleNumber([2,2,1])
assert 4 == Solution().singleNumber([4,1,2,1,2])
assert 1 == Solution().singleNumber([1])
