from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def backtracking(index, current):
            if len(current) == 4:
                if index == len(s):
                    result.append('.'.join(current))
                return

            if index == len(s):
                return

            for length in range(1, 4):
                if index + length > len(s):
                    break

                part = s[index: index+length]

                if len(part) > 1 and part[0] == '0':
                    break

                if int(part) > 255:
                    break

                current.append(part)

                backtracking(index+length, current)

                current.pop()

        backtracking(0, [])
        return result

S = "25525511135"
t = Solution()
re = t.restoreIpAddresses(S)
print(re)
