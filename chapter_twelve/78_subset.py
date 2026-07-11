from typing import List
class Solution:
    def subsets_back(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtracking(index, current):
            result.append(current.copy())
            for i in range(index, len(nums)):
                current.append(nums[i])
                backtracking(i+1, current)
                current.pop()
        
        backtracking(0, [])
        return result
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        for mask in range(1<<n):
            current = []
            for i in range (n):

                if mask & (1<<i):
                    current.append(nums[i])
            result.append(current)
        return result
    
nums = [1,2,3]
#Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
t = Solution()
re = t.subsets(nums)
print(re)