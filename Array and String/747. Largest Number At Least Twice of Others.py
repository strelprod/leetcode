"""You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

 

Example 1:

Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
Example 2:

Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.
Example 3:

Input: nums = [1]
Output: 0
Explanation: 1 is trivially at least twice the value as any other number because there are no other numbers.
"""

from typing import List


# TODO решение без двух циклов: считать максимальное и второе максимальное
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        highest_ix = 0
        highest = nums[highest_ix] / 2
        for ix, val in enumerate(nums):
            curr = val / 2
            if curr > highest:
                highest = curr
                highest_ix = ix

        for ix, val in enumerate(nums):
            if ix != highest_ix and val > highest:
                return -1

        return highest_ix


assert 1 == Solution().dominantIndex([3,6,1,0])
assert -1 == Solution().dominantIndex([1,2,3,4])
assert 0 == Solution().dominantIndex([1])

