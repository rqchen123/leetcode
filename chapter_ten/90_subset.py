from typing import  List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []

        def backtracking(index, current):
            if index == len(nums):
                result.append(current.copy())
                return

            current.append(nums[index])
            backtracking(index + 1, current)
            current.pop()

            while (index +1 < len(nums) and nums[index] == nums[index +1]):
                index += 1
            backtracking(index + 1, current)

        backtracking(0, [])

        return result

t = Solution()
result = t.subsetsWithDup([1, 2, 2])
print('result', result)