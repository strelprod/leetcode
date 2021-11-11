"""We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:

-1: The number I picked is lower than your guess (i.e. pick < num).
1: The number I picked is higher than your guess (i.e. pick > num).
0: The number I picked is equal to your guess (i.e. pick == num).
Return the number that I picked.

 

Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1
Example 4:

Input: n = 2, pick = 2
Output: 2
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

def guess(num: int, ans: int) -> int:
    if num == ans:
        return 0
    elif num < ans:
        return 1
    else:
        return -1


class Solution:
    def guessNumber(self, n: int, pick: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            ans = guess(mid, pick)
            if ans == 0:
                return mid
            elif ans == 1:
                left = mid + 1
            else:
                right = mid - 1
        return -1

assert 6 == Solution().guessNumber(10, 6)
assert 1 == Solution().guessNumber(1, 1)
assert 1 == Solution().guessNumber(2, 1)
assert 2 == Solution().guessNumber(2, 2)