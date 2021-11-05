"""Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.


Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1."""

from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ans = []
        def merge(l, r):
            left_start = 0
            right_start = 0
            res = []
            while left_start < len(l) and right_start < len(r):
                if l[left_start] < r[right_start]:
                    res.append(l[left_start])
                    left_start += 1
                else:
                    res.append(r[right_start])
                    right_start += 1


            while left_start < len(l):
                res.append(l[left_start])
                left_start += 1

            while right_start < len(r):
                res.append(r[right_start])
                right_start += 1
            
            if len(res) >= 3:
                return res[len(res) - 3:len(res)]

            return res

        for ix, val in enumerate(nums):
            if ans and val not in ans:
                ans = merge([val], ans)
            if not ans:
                ans.append(val)

        if len(ans) < 3:
            return max(ans)

        return ans[0]


arr = [3,2,1]
res = 1
assert res == Solution().thirdMax(arr)

arr = [1, 2]
res = 2
assert res == Solution().thirdMax(arr)

arr = [2, 2, 3, 1]
res = 1
assert res == Solution().thirdMax(arr)
