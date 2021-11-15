"""You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

# 1 not bad 
# 2 not bad
# 3 not bad 
# 4 bad

# 1 not bad 
# 2 not bad
# 3 bad 
# 4 bad

# 1 not bad 
# 2 bad
# 3 bad 
# 4 bad

def isBadVersion(version, ans) -> bool:
    return version == ans


class Solution:
    def firstBadVersion(self, n, ans):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            bad = isBadVersion(mid, ans)

            if not bad:
                if isBadVersion(mid + 1, ans):
                    return mid + 1
                else:
                    left = mid + 1
            else:
                right = mid
        
        if left != n + 1 and isBadVersion(left, ans):
            return left
        return -1


class Solution:
    def firstBadVersion(self, n, ans):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2

            if not isBadVersion(mid, ans):
                left = mid + 1
            else:
                right = mid

        return left


assert 4 == Solution().firstBadVersion(4, 4)
assert 3 == Solution().firstBadVersion(4, 3)
assert 2 == Solution().firstBadVersion(4, 2)
assert 4 == Solution().firstBadVersion(5, 4)
assert 1 == Solution().firstBadVersion(1, 1)