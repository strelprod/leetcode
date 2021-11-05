"""Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
"""

from typing import List


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        cnt_max = 0
        
        for val in nums:
            cnt = 0 if val == 0 else cnt + 1
            cnt_max = max(cnt_max, cnt)

        return cnt_max

assert 3 == Solution().findMaxConsecutiveOnes([1,1,0,1,1,1])

assert 2 == Solution().findMaxConsecutiveOnes([1,0,1,1,0,1])