class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for char in s:
            result = result ^ ord(char)
        for char in t:
            result = result ^ ord(char)
        return chr(result)

s = "abcd"
t = "abcde"
te = Solution()
re = te.findTheDifference(s, t)
print(re)
