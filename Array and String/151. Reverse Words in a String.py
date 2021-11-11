"""Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
Example 4:

Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"
Example 5:

Input: s = "Alice does not even like bob"
Output: "bob like even not does Alice"
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        curr_word = []
        for ix in range(len(s)):
            curr_symb = s[ix]
            if curr_symb != " ":
                curr_word.append(curr_symb)
            elif curr_word:
                res.append("".join(curr_word))
                curr_word = []
        if curr_word:
            res.append("".join(curr_word))

        return " ".join(res[::-1])

class Solution:
    def reverseWords(self, s: str) -> str:
        splitted_s = s.split(" ")
        res = list(filter(lambda x: x, splitted_s))
        res_len = len(res)
        ix = 0
        while ix < res_len // 2:
            res[ix], res[res_len - ix - 1] = res[res_len - ix - 1], res[ix]
            ix += 1
        return " ".join(res)



assert "blue is sky the" == Solution().reverseWords("the sky is blue")
assert "world hello" == Solution().reverseWords("  hello world  ")
assert "example good a" == Solution().reverseWords("a good   example")
assert "Alice Loves Bob" == Solution().reverseWords("  Bob    Loves  Alice   ")
assert "bob like even not does Alice" == Solution().reverseWords("Alice does not even like bob")
