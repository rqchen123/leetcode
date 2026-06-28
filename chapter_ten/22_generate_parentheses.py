from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []
        def backtracking(index, current, left_count, right_count):
            if index == 2*n:
                result.append(current)
                return

            if left_count > n or right_count > n or left_count < right_count:
                return

            backtracking(index + 1, current+'(',left_count+1, right_count)
            backtracking(index+1, current+')', left_count, right_count+1)

        backtracking(0, '', 0, 0)
        return result

N = 3
t = Solution()
re = t.generateParenthesis(N)
print(re)