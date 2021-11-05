"""Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

"""

from typing import List


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_len = len(nums)
        ix_order_changed = 0
        for ix in range(nums_len):
            if nums[ix] < 0:
                ix_order_changed = ix
            nums[ix] = nums[ix] ** 2

        res = []

        left_start = ix_order_changed
        right_start = ix_order_changed + 1
        while left_start >= 0 and right_start < nums_len:
            if nums[left_start] < nums[right_start]:
                res.append(nums[left_start])
                left_start -= 1
            else:
                res.append(nums[right_start])
                right_start += 1


        while left_start >= 0:
            res.append(nums[left_start])
            left_start -= 1

        while right_start < nums_len:
            res.append(nums[right_start])
            right_start += 1
        
        return res


arr = [-4,-1,0,3,10]
assert [0,1,9,16,100] == Solution().sortedSquares(arr)

arr = [-7,-3,2,3,11]
assert [4,9,9,49,121] == Solution().sortedSquares(arr)

arr = [-5,-3,-2,-1]
res = Solution().sortedSquares(arr)
assert [1,4,9,25] == res, res