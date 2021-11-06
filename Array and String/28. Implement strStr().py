"""Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:

Input: haystack = "", needle = ""
Output: 0

"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or haystack == needle:
            return 0
        
        haystack_len = len(haystack)
        needle_len = len(needle)

        if haystack_len <= needle_len:
            return -1 

        i = 0
        while i + needle_len <= haystack_len:
            if needle in haystack[i:i + needle_len]:
                return i
            i += 1

        return -1



assert 4 == Solution().strStr(haystack = "mississippi", needle = "issip")
assert 4 == Solution().strStr(haystack = "hlello", needle = "lo")
assert -1 == Solution().strStr(haystack = "aaa", needle = "aaaa")
assert 3 == Solution().strStr(haystack = "hello", needle = "lo")
assert 2 == Solution().strStr(haystack = "hello", needle = "ll")
assert -1 == Solution().strStr(haystack = "aaaaa", needle = "bba")
assert 0 == Solution().strStr(haystack = "", needle = "")
