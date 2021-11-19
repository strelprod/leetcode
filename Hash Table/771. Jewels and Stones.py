"""You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
"""

from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = Counter(stones)
        res = 0
        for stone in jewels:
            if stone in d:
                res += d[stone]
        return res


assert 3 == Solution().numJewelsInStones(jewels = "aA", stones = "aAAbbbb")
assert 0 == Solution().numJewelsInStones(jewels = "z", stones = "ZZ")
