"""Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
Example 2:

Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.
Example 3:

Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.
"""

from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        prepared = {}

        for ix, val in enumerate(arr):
            if val % 2 == 0:
                prepared[val] = ix
        
        for ix, val in enumerate(arr):
            if val * 2 in prepared and prepared[val * 2] != ix:
                return True

        return False


assert True == Solution().checkIfExist([10,2,5,3])

assert True == Solution().checkIfExist([7,1,14,11])

assert False == Solution().checkIfExist([3,1,7,11])
