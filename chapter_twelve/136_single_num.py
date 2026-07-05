from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i = 0
        nums.sort()
        print(nums)
        while i < len(nums) - 1:
            if nums[i] != nums[i+1]:
                print("1111")
                return nums[i]
            i += 2
        return nums[-1]

    def singleNumberB(self, nums:List[int]) -> int:
        result = 0
        for num in nums:
            result = result ^num
            print(f"{num}_result:",result)
        return result


nums_1 = [2,2,1]
#Output: 1

nums_2 = [4,1,2,1,2]
nums_3 = [5, 5, 9]
t = Solution()
re = t.singleNumberB(nums_2)
print(re)
