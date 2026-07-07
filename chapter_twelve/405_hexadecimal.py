class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        hexa = "0123456789abcdef"
        num = num & 0xffffffff

        result = []
        while num >0:
            last_bit = num & 15
            print("last_bit:", last_bit)
            result.append(hexa[last_bit])
            num = num >> 4
        return "".join(reversed(result))


n = 15
t = Solution()
re = t.toHex(n)
print(re)