from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        current_end = 0
        max_reach = 0
        for i in range(len(nums)-1):
            max_reach = max(max_reach, i + nums[i])
            print(f"i={i}, nums[i]={nums[i]}, max_reach={max_reach}, current_end={current_end}, jump={jump}")

            if i == current_end:
                jump += 1
                current_end = max_reach
                print(f"jump now -> jumps={jump}, current_end= {current_end}")
        return jump

nums = [2,3,1,1,4]
t = Solution()
re = t.jump(nums)
print(re)