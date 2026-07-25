from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        heap = []

        for num, freq in count.items():
            heapq.heappush(heap, (num, freq))

            if len(heap)>k:
                heapq.heappop(heap)

        return [num for freq, num in heap]


#Input: 
nums = [1,1,1,2,2,3]
k = 2

#Output: [1,2]
t = Solution()
re = t.topKFrequent(nums, k)

print(re)