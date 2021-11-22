"""A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
"""

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return nums.index(max(nums))
        left = 0
        right = len(nums)
        ans = None
        while left < right:
            mid = (left + right) // 2
            curr = nums[mid]

            if mid == len(nums) - 1:
                right = mid
            elif curr > nums[mid + 1]:
                # right = mid + 1
                return mid
            elif curr < nums[mid + 1]:
                left = mid + 1
    
        return left


            # if mid - 1 >= 0 and nums[mid] > nums[mid - 1]:
            #     left = mid + 1
            # elif mid + 1 < len(nums) and nums[mid] < nums[mid + 1]:
            #     right = mid
            # else:
            #     ans = left
            #     break
        
        return ans


assert 0 == Solution().findPeakElement([6,5,4,3,2,3,2])
assert 0 == Solution().findPeakElement([1])
assert 1 == Solution().findPeakElement([1, 2])
assert 1 == Solution().findPeakElement([1, 2, 1])
assert 2 == Solution().findPeakElement([1, 2, 3])
assert 2 == Solution().findPeakElement([1,2,3,1])
assert Solution().findPeakElement([1,2,3,1,2,1]) in (2, 4)
assert Solution().findPeakElement([1,2,1,3,5,6,4]) in (1, 5)
