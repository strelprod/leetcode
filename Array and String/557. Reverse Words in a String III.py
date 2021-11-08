"""Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        ix = 0
        s_len = len(s)
        res = list(s)
        while ix < s_len // 2:
            res[ix] = s[s_len - ix - 1]
            res[s_len - ix - 1] = s[ix]
            ix += 1
        res = "".join(res).split(" ")
        
        ix = 0
        res_len = len(res)
        while ix < res_len // 2:
            res[ix], res[res_len - ix - 1] = res[res_len - ix - 1], res[ix]
            ix += 1

        return " ".join(res)


class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        word = []
        for val in s:
            if val != " ":
                word.append(val)
            elif word:
                res.append("".join(word[::-1]))
                word = []
        if word:
            res.append("".join(word[::-1]))
        return " ".join(res)


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([val[::-1] for val in s.split(" ")])


assert "ba ca" == Solution().reverseWords("ab ac")
assert "s'teL ekat edoCteeL tsetnoc" == Solution().reverseWords("Let's take LeetCode contest")
assert "doG gniD" == Solution().reverseWords("God Ding")
