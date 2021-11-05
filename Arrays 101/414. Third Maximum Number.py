"""Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.


Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1."""

from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        min_val = float("-inf")
        mid_val = float("-inf")
        max_val = nums[0]
        for val in nums:
            if val > max_val:
                min_val = mid_val
                mid_val = max_val
                max_val = val
            elif mid_val < val < max_val:
                min_val = mid_val
                mid_val = val
            elif min_val < val < mid_val:
                min_val = val

        return min_val if min_val != float("-inf") else max(max_val, mid_val, min_val)


arr = [1, 2]
res = 2
assert res == Solution().thirdMax(arr)

arr = [3,2,1]
res = 1
assert res == Solution().thirdMax(arr)

arr = [1, 2]
res = 2
assert res == Solution().thirdMax(arr)

arr = [2, 2, 3, 1]
res = 1
assert res == Solution().thirdMax(arr)

arr = [3,3,4,3,4,3,0,3,3]
res = 0
assert res == Solution().thirdMax(arr)
