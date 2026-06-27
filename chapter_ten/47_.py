from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        nums.sort()
        result = []
        used = [False] * len(nums)

        def backtracking(index, current):
            if index == len(nums):
                result.append(current.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True

                current.append(nums[i])

                backtracking(index + 1, current)
                current.pop()
                used[i] = False

        backtracking(0,[])
        return result

NUM = [1, 1, 3]
t = Solution()
re = t.permuteUnique(NUM)
print(re)