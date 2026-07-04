
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        char_index = {}

        for right in range(len(s)):
            char = s[right]

            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1

            char_index[char] = right
            max_len = max(max_len, right-left+1)
        return max_len



s = 'abba'
t = Solution()
re = t.lengthOfLongestSubstring(s)
print(re)
