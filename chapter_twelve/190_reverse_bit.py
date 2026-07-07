class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            last_bin = n&1
            result = (result <<1) | last_bin
            n = n >> 1
        return result

n = 1
# output = 2147483648
t = Solution()
re = t.reverseBits(n)
print(re)