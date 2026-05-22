# LeetCode 235: Lowest Common Ancestor of a Binary Search Tree
#
# Description:
# Given a Binary Search Tree root and two nodes p and q,
# find their lowest common ancestor.
#
# Lowest Common Ancestor:
# The lowest node in the tree that has both p and q as descendants.
# A node can be a descendant of itself.
#
# BST Rule:
# All values in the left subtree are smaller than root.val.
# All values in the right subtree are larger than root.val.
#
# Rule:
# If p and q are both smaller than root, go left.
# If p and q are both larger than root, go right.
# Otherwise, root is the lowest common ancestor.
#
# Example:
#
# Tree:
#        6
#       / \
#      2   8
#     / \ / \
#    0  4 7  9
#      / \
#     3   5
#
# Input:  root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
#
# Explanation:
# Node 2 is on the left side of 6.
# Node 8 is on the right side of 6.
# So 6 is their lowest common ancestor.
#
#
# Example 2:
#
# Tree:
#        6
#       / \
#      2   8
#     / \ / \
#    0  4 7  9
#      / \
#     3   5
#
# Input:  root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
#
# Explanation:
# Node 2 is an ancestor of node 4.
# A node can be an ancestor of itself.
# So the lowest common ancestor is 2.
#
#
# Thinking:
#
# Current root:
#       root
#      /    \
#   left    right
#
# Case 1:
# If p and q are both smaller than root:
#       root
#      /
#   p and q
#
# Go left.
#
# Case 2:
# If p and q are both larger than root:
#       root
#           \
#          p and q
#
# Go right.
#
# Case 3:
# If p and q are on different sides,
# or root is p or q:
#       root
#      /    \
#     p      q
#
# Return root.

# Definition for a binary tree node.
import ut_tree as ut

TREE = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


# LeetCode 235: Lowest Common Ancestor of a Binary Search Tree
#
# Description:
# Given a Binary Search Tree root and two nodes p and q,
# find their lowest common ancestor.
#
# Lowest Common Ancestor:
# The lowest node in the tree that has both p and q as descendants.
# A node can be a descendant of itself.
#
# BST Rule:
# All values in the left subtree are smaller than root.val.
# All values in the right subtree are larger than root.val.
#
# Rule:
# If p and q are both smaller than root, go left.
# If p and q are both larger than root, go right.
# Otherwise, root is the lowest common ancestor.
#
# Example:
#
# Tree:
#        6
#       / \
#      2   8
#     / \ / \
#    0  4 7  9
#      / \
#     3   5
#
# Input:  root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
#
# Explanation:
# Node 2 is on the left side of 6.
# Node 8 is on the right side of 6.
# So 6 is their lowest common ancestor.
#
#
# Example 2:
#
# Tree:
#        6
#       / \
#      2   8
#     / \ / \
#    0  4 7  9
#      / \
#     3   5
#
# Input:  root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
#
# Explanation:
# Node 2 is an ancestor of node 4.
# A node can be an ancestor of itself.
# So the lowest common ancestor is 2.
#
#
# Thinking:
#
# Current root:
#       root
#      /    \
#   left    right
#
# Case 1:
# If p and q are both smaller than root:
#       root
#      /
#   p and q
#
# Go left.
#
# Case 2:
# If p and q are both larger than root:
#       root
#           \
#          p and q
#
# Go right.
#
# Case 3:
# If p and q are on different sides,
# or root is p or q:
#       root
#      /    \
#     p      q
#
# Return root.

# Definition for a binary tree node.
import ut_tree as ut

TREE = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


if __name__ == "__main__":
    root = ut.build_tree(TREE)

    p = ut.find_node(root, 2)
    q = ut.find_node(root, 4)

    solution = Solution()
    result = solution.lowestCommonAncestor(root, p, q)

    print()
    print(f"p = {p.val}")
    print(f"q = {q.val}")
    print(f"LCA = {result.val}")

