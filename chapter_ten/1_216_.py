from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        nums = list(range(1, 10))
        result = []


        def backtracking(index, current):
            if len(current) == k:
                if sum(current) == n:
                    result.append(current.copy())
                return

            if index == len(nums):
                return
            current.append(nums[index])
            backtracking(index+1, current)
            current.pop()
            backtracking(index+1, current)

        backtracking(0, [])
        return result
K = 3
N = 7
t = Solution()
re = t.combinationSum3(K, N)
print(re)
