"""Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for val in nums1:
            if val not in d:
                d[val] = (1, 0)
            else:
                d[val] = (d[val][0] + 1, 0)
        
        for val in nums2:
            if val in d:
                d[val] = (d[val][0], d[val][1] + 1)
        
        ans = []
        for k, v in d.items():
            i1, i2 = v
            while i1 > 0 and i2 > 0:
                ans.append(k)
                i1 -= 1
                i2 -= 1
        return ans


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for val in nums1:
            if val not in d:
                d[val] = 1
            else:
                d[val] += 1
        
        ans = []
        for val in nums2:
            if val in d and d[val] > 0:
                ans.append(val)
                d[val] -= 1
        return ans


assert [2,2] == Solution().intersect(nums1 = [1,2,2,1], nums2 = [2,2])
assert [4,9] == sorted(Solution().intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
# 1: 2, 0
# 2: 2, 2

# 4: 1, 2
# 5: 1, 0
# 9: 1, 2
