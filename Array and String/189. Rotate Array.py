"""Given an array, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

from typing import List

# TODO
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        if not k or nums_len == 1:
            return nums
        
        ix = nums_len - k - 1
        while ix >= 0:
            nums[ix], nums[ix + k] = nums[ix + k], nums[ix]
            ix -= 1

        last_cnt = (nums_len - k) % k
        if last_cnt == 0:
            return nums

        # порядок подмассива k может быть разный TODO
        # ix = last_cnt - 1
        # iy = k - last_cnt - 1
        # print(nums)
        # while ix < last_cnt:
        #     nums[ix], nums[iy] = nums[iy], nums[ix]
        #     ix -= 1
        #     iy -= 1

        
        
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        if not k or nums_len == 1:
            return nums
        
        def rotate(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1 

        rotate(nums_len - k, nums_len - 1)
        rotate(0, nums_len - k - 1)
        rotate(0, nums_len -1)



nums = [1,2,3,4,5,6]
Solution().rotate(nums, k = 11)
assert [2,3,4,5,6,1] == nums, nums
nums = [12,11, 13, 1,2,3,4,5,6,7]
Solution().rotate(nums, k = 4)
assert [4,5,6,7,12,11, 13, 1,2,3] == nums, nums
nums = [1,2,3,4,5,6,7]
Solution().rotate(nums, k = 3)
assert [5,6,7,1,2,3,4] == nums, nums
nums = [-1,-100,3,99]
Solution().rotate(nums, k = 2)
assert [3,99,-1,-100] == nums, nums
        