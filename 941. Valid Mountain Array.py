"""Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
"""

from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        top_ix = 0
        for ix in range(1, len(arr)):
            if arr[ix - 1] < arr[ix]:
                continue
            top_ix = ix - 1
            if arr[ix - 1] <= arr[ix]:
                return False
            
            break

        for ix in range(top_ix + 1, len(arr)):
            if arr[ix - 1] > arr[ix]:
                continue
            if arr[ix - 1] <= arr[ix]:
                return False

        if top_ix:
            return True
        return False


assert False == Solution().validMountainArray([2,1])

assert False == Solution().validMountainArray([3,5,5])

assert True == Solution().validMountainArray([0,3,2,1])
