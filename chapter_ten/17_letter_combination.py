from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return None

        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []

        def backtracking(index, current):
            if index == len(digits):
                result.append(current)
                return

            current_digit = digits[index]
            for letter in phone_map[current_digit]:
                backtracking(index+1, current+letter)

        backtracking(0, '')
        print(result)


t = Solution()
t.letterCombinations(digits='23')