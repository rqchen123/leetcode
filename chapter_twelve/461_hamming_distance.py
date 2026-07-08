class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count("1")

x = 1
y = 4
#Output: 2
t = Solution()
re = t.hammingDistance(x, y)
print(re)
