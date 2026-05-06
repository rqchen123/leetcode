# Topic: Recursion / Memoization
# Problem: 1137. N-th Tribonacci Number
# Link: https://leetcode.com/problems/n-th-tribonacci-number/


class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def dfs(num: int) -> int:
            if num == 0:
                return 0

            if num == 1 or num == 2:
                return 1

            if num in memo:
                return memo[num]

            memo[num] = dfs(num - 1) + dfs(num - 2) +dfs(num-3)
            return memo[num]

        return dfs(n)


if __name__ == "__main__":
    s = Solution()
    print(s.tribonacci(4))
