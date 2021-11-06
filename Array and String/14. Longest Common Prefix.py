"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

from typing import List

# TODO изучить решения https://leetcode.com/problems/longest-common-prefix/solution/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        smallest_str_len = float("-inf")
        smallest_str_ix = None
        for ix, curr_str in enumerate(strs):
            l = len(curr_str)
            if l > smallest_str_len:
                smallest_str_len = l
                smallest_str_ix = ix

        cnt_str = len(strs)
        i = 0
        longest_str = []
        for ix, curr_str in enumerate(strs[smallest_str_ix]):
            j = 0
            while j < cnt_str:
                if ix < len(strs[j]) and strs[j][ix] == curr_str:
                    j += 1
                else:
                    j = 0
                    break
            if j > 0:
                longest_str.append(curr_str)
            else:
                break

        return "".join(longest_str)



assert "flo" == Solution().longestCommonPrefix(["flow","flo"])
assert "fl" == Solution().longestCommonPrefix(["flower","flow","flight"])
assert "" == Solution().longestCommonPrefix(["dog","racecar","car"])
assert "c" == Solution().longestCommonPrefix(["cir","car"]), Solution().longestCommonPrefix(["cir","car"])
