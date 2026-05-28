# LeetCode 124: Binary Tree Maximum Path Sum
#
# Description:
# Given the root of a binary tree, return the maximum path sum.
#
# A path is any sequence of nodes where each pair of adjacent nodes has an edge.
# The path does not need to pass through the root.
# The path must contain at least one node.
#
# Rule:
# At each node, we think about two different things:
#
# 1. The best path that passes through the current node:
#
#        left
#          \
#          root
#          /
#       right
#
#    Sum = left_gain + root.val + right_gain
#
#    This is used to update the global maximum answer.
#
#
# 2. The best path we can return to the parent:
#
#          root
#          /
#       left
#
#    or
#
#          root
#            \
#            right
#
#    We can only return one side to the parent, because a path cannot split upward.
#
#
# Important:
# If the left or right path sum is negative, we ignore it by using 0.
#
# Example:
#
# Original tree:
#        -10
#        /  \
#       9   20
#          /  \
#         15   7
#
# Best path:
#        15
#          \
#          20
#            \
#             7
#
# Maximum path sum:
# 15 + 20 + 7 = 42
#
# Input:  root = [-10,9,20,null,null,15,7]
# Output: 42
#
#
# Now we are coming back from recursion.
#
# Example 2:
#
# Original tree:
#              5
#             / \
#            4   8
#           /   / \
#         11   13  4
#        /  \       \
#       7    2       1
#
# Input:
# root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
#
# Best path:
#
#       7
#        \
#        11
#          \
#           4
#            \
#             5
#              \
#               8
#              /
#            13
#
# Maximum path sum:
# 7 + 11 + 4 + 5 + 8 + 13 = 48
#
# Output: 48
#
# Explanation:
# The best path does not need to start from the root.
# The best path does not need to end at a leaf.
# It only needs to be connected by parent-child edges.
#
# At node 5:
#
# left_gain = 4 + 11 + 7 = 22
# right_gain = 8 + 13 = 21
#
# current_path = 5 + 22 + 21 = 48
#
# So the answer is 48.

from typing import Optional
import ut_tree
#        -10
#        /  \
#       9   20
#          /  \
#         15   7
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            current_path = node.val + left_gain + right_gain

            self.max_sum = max(self.max_sum, current_path)
            return node.val + max(left_gain, right_gain)
        dfs(root)
        return self.max_sum


Tree=[-10, 9, 20, None, None, 15, 7]
root = ut_tree.build_tree(Tree)
print('root:', root)
answer = Solution().maxPathSum(root)
print("answer:", answer)


