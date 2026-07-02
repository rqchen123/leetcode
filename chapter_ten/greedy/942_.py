from typing import List

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low = 0
        high = len(s)
        result = []

        for char in s:
            if char == "D":
                result.append(high)
                high -= 1
            else:
                result.append(low)
                low += 1
        result.append(low)
        return result

s = "IDID"
t = Solution()
re = t.diStringMatch(s)
print(re)