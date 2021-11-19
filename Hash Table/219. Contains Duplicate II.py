"""Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

from typing import List
from collections import Counter

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for ix, val in enumerate(nums):
            if val in d and ix - d[val] <= k:
                return True
            else:
                d[val] = ix

        return False


assert True == Solution().containsNearbyDuplicate(nums = [0,1,1,1], k = 2)
assert True == Solution().containsNearbyDuplicate(nums = [2,2,2], k = 3)
assert True == Solution().containsNearbyDuplicate(nums = [1,2,3,1], k = 3)
assert True == Solution().containsNearbyDuplicate(nums = [1,0,1,1], k = 1)
assert False == Solution().containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2)
