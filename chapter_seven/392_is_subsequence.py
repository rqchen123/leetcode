# LeetCode 392: Is Subsequence

# Description:

# Given two strings s and t,

# return True if s is a subsequence of t.

# Otherwise, return False.

#

# A subsequence is formed by deleting some characters

# without changing the order of the remaining characters.

#

# Example 1:

# Input: s = "abc", t = "ahbgdc"

# Output: True

#

# Explanation:

# The characters a, b, and c appear in t

# in the same order.

#

# Example 2:

# Input: s = "axc", t = "ahbgdc"

# Output: False

#

# Explanation:

# The character x does not appear in t.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        print(m)
        return m == dp[m][n]

s ="abc"
t ="ahbgdc"
t = Solution().isSubsequence(s, t)
