class Solution:
    def isPowerOfFour_math(self, n: int) -> bool:
        if n<= 0:
            return False

        while n > 1:
            print('n:', n)
            if n %4 != 0:
                return False
            n = n//4
        return True
    
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and (n&(n-1)==0) and (n & 0x55555555) !=0

n = 15
t = Solution()
re = t.isPowerOfFour(n)
print(re)