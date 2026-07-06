class Solution:
    def hammingWeight_math(self, n: int) -> int:
        count = 0
        while n > 0:
            print(f"count:{count},n:", n)
            if n%2 == 1:
                count += 1

            n = n // 2

        print("final:", count)
        return count
    
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            if n & 1:
                count += 1
            n = n >> 1
        return count 

n = 8
t = Solution()
re = t.hammingWeight(n)
print(re)