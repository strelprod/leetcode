"""Write a function that reverses a string. The input string is given as an array of characters s.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s:
            return
        
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


s = ["h","e","l","l","o"]
Solution().reverseString(s)
res = ["o","l","l","e","h"]
assert s == res

s = ["H","a","n","n","a","h"]
Solution().reverseString(s)
res = ["h","a","n","n","a","H"]
assert s == res
