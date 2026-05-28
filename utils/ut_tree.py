from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


def get_height(root):
    if not root:
        return 0

    left_height = get_height(root.left)
    right_height = get_height(root.right)

    return 1 + max(left_height, right_height)


def print_tree(root):
    if isinstance(root, list):
        root = build_tree(root, show=False)

    if not root:
        print("(empty tree)")
        return

    height = get_height(root)
    level_nodes = [root]

    for level in range(height):
        indent = 2 ** (height - level - 1) - 1
        between = 2 ** (height - level) - 1

        line = " " * indent
        next_nodes = []

        for node in level_nodes:
            if node:
                line += str(node.val)
                next_nodes.append(node.left)
                next_nodes.append(node.right)
            else:
                line += " "
                next_nodes.append(None)
                next_nodes.append(None)

            line += " " * between

        print(line.rstrip())

        if level < height - 1:
            branch_indent = 2 ** (height - level - 2) - 1
            branch_between = 2 ** (height - level - 1) - 1

            branch_line = " " * branch_indent

            for node in level_nodes:
                if node:
                    branch_line += "/" if node.left else " "
                    branch_line += " " * branch_between
                    branch_line += "\\" if node.right else " "
                else:
                    branch_line += " "
                    branch_line += " " * branch_between
                    branch_line += " "

                branch_line += " " * branch_between

            print(branch_line.rstrip())

        level_nodes = next_nodes


def build_tree(values, show=True):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    if show:
        print("Tree:")
        print_tree(root)

    return root


def find_node(root, target):
    if not root:
        return None

    if root.val == target:
        return root

    left = find_node(root.left, target)
    if left:
        return left

    return find_node(root.right, target)


def build_test_case(values, p_val, q_val, show=True):
    root = build_tree(values, show=show)

    p = find_node(root, p_val)
    q = find_node(root, q_val)

    if show:
        print()
        print(f"p = {p.val if p else None}")
        print(f"q = {q.val if q else None}")

    return root, p, q