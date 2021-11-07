"""Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # if target in nums:
        #     return 1
        # total_sum = sum(nums)
        # if total_sum < target:
        #     return 0
        # len_nums = len(nums)
        # if total_sum == target:
        #     return len_nums

        ix_min_len = float("inf")
        total_sum = 0
        slower_pointer = 0
        for faster_pointer, val in enumerate(nums):
            total_sum += val
            while total_sum >= target:
                ix_curr_len = faster_pointer - slower_pointer + 1
                total_sum -= nums[slower_pointer]
                slower_pointer += 1
                if ix_curr_len < ix_min_len:
                    ix_min_len = ix_curr_len
        
        return 0 if ix_min_len == float("inf") else ix_min_len


assert 2 == Solution().minSubArrayLen(7, [2,3,1,2,4,3])
assert 1 == Solution().minSubArrayLen(4, [1, 4, 4])
assert 0 == Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1])
