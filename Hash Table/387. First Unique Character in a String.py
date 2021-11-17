"""Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for ix, char in enumerate(s):
            if char in d:
                d[char] = (ix, d[char][1] + 1)
            else:
                d[char] = (ix, 1)

        for k, v in d.items():
            if v[1] == 1:
                return v[0]
        
        return -1


from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)

        for ix, char in enumerate(s):
            if c[char] == 1:
                return ix
        
        return -1




assert 0 == Solution().firstUniqChar("leetcode")
assert 2 == Solution().firstUniqChar("loveleetcode")
assert -1 == Solution().firstUniqChar("aabb")
