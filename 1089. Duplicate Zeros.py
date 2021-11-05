"""Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

 

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
"""

from typing import List

# TODO сделать space - o(1)
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if sum(arr) == 0:
            return
        arr_len = len(arr)
        ix = 0
        arr_modified = []
        while ix < arr_len:
            curr_val = arr[ix]
            if curr_val == 0:
                arr_modified.append(0)
                arr_modified.append(0)
            else:
                arr_modified.append(curr_val)
            ix += 1
        for ix in range(len(arr)):
            arr[ix] = arr_modified[ix]

arr = [1,0,2,3,0,4,5,0]
res = [1,0,0,2,3,0,0,4]
Solution().duplicateZeros(arr)
assert res == arr

arr = [1,2,3]
res = [1,2,3]
Solution().duplicateZeros(arr)
assert res == arr
