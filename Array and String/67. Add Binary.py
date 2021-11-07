"""Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_len = len(a)
        b_len = len(b)
        if a_len < b_len:
            a, b = b, a
            a_len, b_len = b_len, a_len
        
        new_b = []
        for ix in range(a_len - b_len):
            new_b.append("0") 
        for ix in range(b_len):
            new_b.append(b[ix])
            
        b = "".join(new_b)

        i_b = a_len - 1
        next_digit = 0
        res = []

        while i_b >= 0:
            if a[i_b] == "1" and b[i_b] == "1":
                if next_digit:
                    next_digit = 1
                    res.append("1")
                else:
                    res.append("0")
                    next_digit = 1
            elif a[i_b] == "1" and b[i_b] == "0" or a[i_b] == "0" and b[i_b] == "1":
                if next_digit:
                    next_digit = 1
                    res.append("0")
                else:
                    res.append("1")
            else:
                if next_digit:
                    next_digit = 0
                    res.append("1")
                else:
                    res.append("0")
            i_b -= 1
        if next_digit:
            res.append("1")

        return "".join(res[::-1])


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_pointer = len(a) - 1
        b_pointer = len(b) - 1
        total_sum = 0
        res = []
        while a_pointer >= 0 or b_pointer >= 0:
            curr_sum = total_sum
            if a_pointer >= 0:
                curr_sum += int(a[a_pointer])
                a_pointer -= 1
            if b_pointer >= 0:
                curr_sum += int(b[b_pointer])
                b_pointer -= 1
            res.append(str(curr_sum % 2))
            total_sum = curr_sum // 2
        
        if total_sum:
            res.append("1")
        
        return "".join(res[::-1])



assert "1000" == Solution().addBinary(a = "1", b = "111")
assert "10" == Solution().addBinary(a = "1", b = "1")
assert "11" == Solution().addBinary(a = "10", b = "1")
assert "100" == Solution().addBinary(a = "11", b = "1")
assert "101" == Solution().addBinary(a = "11", b = "10")
assert "10101" == Solution().addBinary(a = "1010", b = "1011")
