"""Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
"""

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows < 1:
            return res[:numRows]
        row = 0
        while row < numRows - 1:
            next_res = [1]
            prev_row_len = len(res[row])
            for ix in range(prev_row_len):
                if ix == prev_row_len - 1:
                    next_res.append(1)
                else:
                    next_res.append(res[row][ix] + res[row][ix + 1])
            row += 1
            res.append(next_res)
        return res


assert [[1]] == Solution().generate(1)
assert [[1],[1,1]] == Solution().generate(2), Solution().generate(2)
assert [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]] == Solution().generate(5), Solution().generate(5)

