"""There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_len = len(nums) - 1
        
        pivot_index = 0

        left = 0
        right = nums_len

        if nums_len + 1 == 2:
            return nums.index(target) if target in nums else -1


        while left < right:
            mid = (left + right) // 2
            if mid - 1 >= 0 and mid + 1 <= right:
                if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                    pivot_index = mid
                    break
                elif nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                    pivot_index = mid + 1
                    break
                elif nums[mid - 1] < nums[mid] < nums[mid + 1]:
                    if nums[0] > nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
            elif mid == 0:
                if nums[mid] > nums[mid + 1]:
                    pivot_index = mid + 1
                    break


        if pivot_index == 0:
            left = 0
            right = nums_len
        elif nums[0] > target:
            left = pivot_index
            right = nums_len
        else:
            left = 0
            right = pivot_index
            
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1


assert 4 == Solution().search(nums = [5,1,2,3,4], target = 4)
assert 0 == Solution().search(nums = [6,7,1,2,3,4,5], target = 6)
assert 2 == Solution().search(nums = [5, 1, 3], target = 3)
assert 2 == Solution().search(nums = [1, 3, 5], target = 5)
assert -1 == Solution().search(nums = [1, 2, 3], target = 5)
assert 0 == Solution().search(nums = [5, 1, 3], target = 5)
assert 0 == Solution().search(nums = [3,4, 5, 1], target = 3)
assert 0 == Solution().search(nums = [3,4, 5, 1,2], target = 3)
assert 1 == Solution().search(nums = [1, 3], target = 3)
assert 0 == Solution().search(nums = [1, 3], target = 1)
assert -1 == Solution().search(nums = [1, 3], target = 0)
assert 4 == Solution().search(nums = [4,5,6,7,0,1,2], target = 0)
assert -1 == Solution().search([4,5,6,7,0,1,2], target = 3)
assert -1 == Solution().search(nums = [1], target = 0)

