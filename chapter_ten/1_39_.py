from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        result = []

        def backtracking(index, current):
            if sum(current) == target:
                result.append(current.copy())
                return
            if sum(current) > target:
                return
            if index == len(candidates):
                return

            current.append(candidates[index])
            backtracking(index, current)
            current.pop()
            backtracking(index+1, current)

        backtracking(0, [])

        return result

NUM = [2, 3, 6, 7]
TARGET = 7
t = Solution()
re = t.combinationSum(NUM, TARGET)
print(re)