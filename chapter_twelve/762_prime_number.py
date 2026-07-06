class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0

        for num in range(left, right + 1):
            binary = bin(num)
            one = binary.count("1")

            if one in [2, 3, 5, 7, 11, 13, 15, 17, 19]:
                count += 1
        return count


left = 6
right = 10
#Output: 4
t = Solution()
re = t.countPrimeSetBits(left, right)
print(re)