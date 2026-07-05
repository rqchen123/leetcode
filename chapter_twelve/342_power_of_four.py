class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<= 0:
            return False

        while n > 1:
            print('n:', n)
            if n %4 != 0:
                return False
            n = n//4
        return True

n = 3
t = Solution()
re = t.isPowerOfFour(n)
print(re)