# Topic: Stack / Monotonic Stack
# Problem: 496. Next Greater Element I
# Link: https://leetcode.com/problems/next-greater-element-i/


from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        for num in nums2:
            while stack and stack[-1] < num:
                old_num = stack.pop()
                next_greater[old_num] = num

            stack.append(num)

        while stack:
            old_num = stack.pop()
            next_greater[old_num] = -1

        result = []

        for num in nums1:
            result.append(next_greater[num])

        return result