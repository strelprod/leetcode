"""Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

 

Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
"""

# TODO
class Solution:
    def mySqrt(self, x: int) -> int:
        if x in (0, 1):
            return x
        left = 0
        right = x - 1
        mid = 1
        while left < right:
            mid = (left + right) // 2
            mid_2 = mid * mid
            if mid_2 == x:
                return mid
            elif mid_2 > x:
                right = mid - 1
            else:
                left = mid + 1
        return mid

        
#assert 1 == Solution().mySqrt(3)
assert 2 == Solution().mySqrt(8)
assert 2 == Solution().mySqrt(4)
assert 3 == Solution().mySqrt(9)
assert 1 == Solution().mySqrt(1)
assert 0 == Solution().mySqrt(0)
