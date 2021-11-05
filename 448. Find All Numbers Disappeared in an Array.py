"""Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
 

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for ix, val in enumerate(nums):
            ix = abs(val) - 1
            if nums[ix] > 0:
                nums[ix] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)

        return res


nums = [4,3,2,7,8,2,3,1]
res = [5, 6]
assert sorted(res) == sorted(Solution().findDisappearedNumbers(nums))

nums = [1,1]
res = [2]
assert sorted(res) == sorted(Solution().findDisappearedNumbers(nums))
