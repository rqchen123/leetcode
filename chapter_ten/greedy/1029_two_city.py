from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: (x[0]- x[1]))
        print("costs:", costs)

        n = len(costs) //2
        total = 0

        for i in range(len(costs)):
            if i < n:
                total += costs[i][0]
                print(f"n:{n}, total:{total}")
            else:
                total += costs[i][1]

        return total
costs = [[10,20],[30,200],[400,50],[30,20]]
t = Solution()
re = t.twoCitySchedCost(costs)
# 30+10+20+50=110
print(re)