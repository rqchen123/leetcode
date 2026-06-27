from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        result = []
        print("1___")

        def backtracking(index, current):
            if index == len(nums):
                result.append(current.copy())
                return

            current.append(nums[index])
            backtracking(index + 1, current)
            print("current:", current)
            current.pop()
            backtracking(index +1, current)

        backtracking(0, [])
        print("result:", result)
        return result

t = Solution()
result = t.subsets([1, 2, 3])