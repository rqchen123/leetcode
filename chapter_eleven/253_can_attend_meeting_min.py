## Leetcode 253. Meeting Rooms II (Medium)

#Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...]
#  (start_i < end_i), find the minimum number of rooms required to schedule all meetings without any conflicts.

#Note: (0,8),(8,10) is NOT considered a conflict at 8.

#- Example 1:

#Input: intervals = [(0,40),(5,10),(15,20)]

#Output: 2

#Explanation:
#room1: (0,40)
#room2: (5,10),(15,20)

#- Example 2:

#Input: intervals = [(4,9)]

#Output: 1

from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return 0
        
        starts = sorted(interval[0] for interval in intervals)
        ends = sorted(interval[1] for interval in intervals)

        start_pointer = 0
        end_pointer = 0

        rooms_in_use = 0
        max_rooms = 0

        while start_pointer < len(intervals):
            if starts[start_pointer] < ends[end_pointer]:
                rooms_in_use += 1
                max_rooms = max(max_rooms, rooms_in_use)
                start_pointer += 1
            else:
                rooms_in_use -= 1
                end_pointer += 1

        return max_rooms



#intervals = [(0,30),(5,10),(15,20)]
intervals = [(5,8),(9,15)]
t = Solution()
re = t.minMeetingRooms(intervals)
print(re)