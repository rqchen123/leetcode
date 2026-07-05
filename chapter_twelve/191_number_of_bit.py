class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            print(f"count:{count},n:", n)
            if n%2 == 1:
                count += 1

            n = n // 2

        print("final:", count)
        return count

n = 11
t = Solution()
re = t.hammingWeight(n)