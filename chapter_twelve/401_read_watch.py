from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []

        for hour in range(12):
            for minute in range(60):
                light = bin(hour).count("1") + bin(minute).count("1")

                if light == turnedOn:
                    result.append(f"{hour}:{minute:02d}")
        return result

turnedOn = 1
#Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
t = Solution()
re = t.readBinaryWatch(turnedOn)
print("re:", re)