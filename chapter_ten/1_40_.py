from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        result = []
        candidates.sort()
        def backtracking(index, current):
            if sum(current) == target:
                result.append(current.copy())
                return
            if sum(current) > target:
                return
            if index == len(candidates):
                return

            current.append(candidates[index])
            backtracking(index+1, current)
            current.pop()

            while (index + 1 < len(candidates) and candidates[index] == candidates[index+1]):
                index += 1

            backtracking(index+1, current)

        backtracking(0, [])
        return result

NUM = [10, 1, 2, 7, 6, 1, 5]
TARGET = 8
t = Solution()
re = t.combinationSum2(NUM, TARGET)
print(re)
