# LeetCode 156: Binary Tree Upside Down
#
# Description:
# Given a binary tree where every right node is either a leaf node with a sibling
# or empty, turn the tree upside down.
#
# Rule:
# The original left child becomes the new parent.
# The original right child becomes the new left child.
# The original root becomes the new right child.
#
# Example:
#
# Original tree:
#        1
#       / \
#      2   3
#     / \
#    4   5
#
# Upside-down tree:
#        4
#       / \
#      5   2
#         / \
#        3   1
#
# Input:  root = [1,2,3,4,5]
# Output: [4,5,2,null,null,3,1]


# Now we are coming back from recursion.
#
# Original:
#       root
#      /    \
#   left    right
#
# New:
#       left
#      /    \
#   right   root
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def upsideDownBinaryTree(self, root):
        if not root or not root.left:
            return root

        new_root = self.upsideDownBinaryTree(root.left)

        root.left.left = root.right
        root.left.right = root

        # cut old links to avoid cycle.
        root.left = None
        root.right = None
        return new_root


def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i< len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)

        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)

        i += 1

    return root


def tree_to_list(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    return result

root = build_tree([1, 2, 3, 4, 5])

solution = Solution()
new_root = solution.upsideDownBinaryTree(root)
print(tree_to_list(new_root))



