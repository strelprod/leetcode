"""Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        key_counter = Counter(nums)
        cnt_counter = {}
        curr_max = [float("-inf"), float("-inf"), float("-inf")]

        for key in key_counter:
            if key_counter[key] not in cnt_counter:
                cnt_counter[key_counter[key]] = [key]
                
                if key_counter[key] > curr_max[0]:
                    curr_max[2] = curr_max[1]
                    curr_max[1] = curr_max[0]
                    curr_max[0] = key_counter[key]
                elif curr_max[1] < key_counter[key] < curr_max[0]:
                    curr_max[2] = curr_max[1]
                    curr_max[1] = key_counter[key]
                elif curr_max[2] < key_counter[key] < curr_max[1]:
                    curr_max[2] = key_counter[key]

            else:
                cnt_counter[key_counter[key]].append(key)

        ans = []
        ix = 0
        while len(ans) < k:
            vals = cnt_counter[curr_max[ix]]
            can_put = k - len(ans)
            ans.extend(vals[:can_put])
            ix += 1
            
        return ans


assert [1, 2, 3] == Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 3)
assert [1, 2] == Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2)
assert [1] == Solution().topKFrequent(nums = [1], k = 1)
