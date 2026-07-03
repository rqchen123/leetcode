from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False

            max_reach = max(max_reach, i + nums[i])
        return True

nums_1 = [2,3,1,1,4]
nums_2 = [3,2,1,0,4]

t = Solution()
re = t.canJump(nums_1)

print("re:", re)