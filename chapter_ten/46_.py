from typing import  List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        result = []

        def backtracking(index, current):
            if index == len(nums):
                result.append(current.copy())
                return
            # index = 0, current=[], for num in nums, it will use 1, , current=[1], backtracking(1, [1]), so 1 is in nums,
            # then it will use num=2, current.append(num), current=[1, 2], backtracking(2, [1,2], then it will continue
            # backtracking(3, [1, 2]then before first pop it will be current=[1, 2, 3] then it will pop 3, then current=[1, 2]
            # this is what i understood.


            for num in nums:
                if num in current:
                    continue

                current.append(num)
                backtracking(index+1, current)
                breakpoint()
                print(current)
                current.pop()

        backtracking(0, [])
        return result

t = Solution()
re = t.permute([1, 2, 3])
print(re)