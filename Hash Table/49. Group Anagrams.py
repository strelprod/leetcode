"""Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for str_ in strs:
            sorted_str = "".join(sorted(str_))
            if sorted_str in d:
                d[sorted_str].append(str_)
            else:
                d[sorted_str] = [str_]

        return [v for k, v in d.items()]


assert [[""]] == Solution().groupAnagrams([""])
assert [["a"]] == Solution().groupAnagrams(["a"])
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# assert sorted([["bat"],["nat","tan"],["ate","eat","tea"]]) == Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
