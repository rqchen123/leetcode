from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        result = []

        for current in intervals:
            if not result or current[0] > result[-1][1]:
                print("if_current:", current)
                result.append(current)
            else:
                result[-1][1] = max(result[-1][1], current[1])
        return result


intervals = [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
t = Solution()
re = t.merge(intervals)
print(re)