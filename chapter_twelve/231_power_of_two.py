class Solution:
    def isPowerOfTwo_math(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 1:
            if n % 2 != 0:
                return False
            n = n // 2
        return True
    
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (n&(n-1) == 0)


n = 8
#Output: true
t = Solution()
re = t.isPowerOfTwo(n)
print(re)