from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        max_area = 0
        while left < right:
            height_a = min(height[left], height[right])
            length_b = right - left
            current_area = height_a * length_b

            max_area = max(current_area, max_area )
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return max_area

height = [1,8,6,2,5,4,8,3,7]
t = Solution()
re = t.maxArea(height)
print(re)
