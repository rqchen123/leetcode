## Leetcode 252. Meeting Rooms

#Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...]
#  (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

#Note: (0,8),(8,10) is not considered a conflict at 8

#- Example 1:

#Input: intervals = [(0,30),(5,10),(15,20)]

#Output: false

#Explanation:

#(0,30) and (5,10) will conflict
#(0,30) and (15,20) will conflict
#- Example 2:

#Input: intervals = [(5,8),(9,15)]
#Output: true

from typing import List

class Solution:
    def canAttendMeeting_solution(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda intervals: intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True
    
    def canAttendMeeting(self, intervals: List[List[int]]) -> bool:
        start = sorted([interval[0] for interval in intervals])
        end = sorted([interval[1] for interval in intervals])

        start_points = 0
        end_points = 0
        room_in_use = 0
     

        while start_points < len(intervals):
            print("start_points:", start_points)
            if start[start_points] < end[end_points]:
                room_in_use += 1
                start_points += 1
                if room_in_use > 1:
                    return False
            else:
                room_in_use -= 1
                end_points += 1
        return True


intervals = [(0,30),(5,10),(15,20)]
#intervals = [(5,8),(9,15)]
t = Solution()
re = t.canAttendMeeting(intervals)
print(re)