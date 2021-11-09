"""Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
"""

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] * (rowIndex + 1)
        row = 0
        while row < rowIndex:
            ix = row
            while ix - 1 >= 0:
                res[ix] = res[ix] + res[ix - 1]
                ix -= 1
            row += 1

        return res
        

# assert [1] == Solution().getRow(0)
# assert [1,1] == Solution().getRow(1)
# assert [1,2,1] == Solution().getRow(2)
assert [1,3,3,1] == Solution().getRow(3)
