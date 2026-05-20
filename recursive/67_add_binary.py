# Topic: Recursion
# Problem: 67. Add Binary
# Link: https://leetcode.com/problems/add-binary/

import sys

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sys.setrecursionlimit(max(len(a), len(b)) + 10)

        result = []

        def dfs(i: int, j: int, carry: int) -> None:
            if i < 0 and j < 0 and carry == 0:
                return

            total = carry

            if i >= 0:
                total += int(a[i])

            if j >= 0:
                total += int(b[j])

            current_digit = total % 2
            new_carry = total // 2

            result.append(str(current_digit))

            dfs(i-1, j-1, new_carry)

        dfs(len(a) - 1, len(b) - 1, 0)

        return "".join(result[::1])

run = Solution()
run.addBinary('11', '10')