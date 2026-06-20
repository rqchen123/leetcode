import ut_node as ut


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


# Build: 4 -> 5 -> 1 -> 9
head = ut.build_linked_list([4, 5, 1, 9])

print("Before:")
ut.print_linked_list(head)

# Find the actual node object containing 5
node_to_delete = ut.find_node(head, 5)

solution = Solution()
solution.deleteNode(node_to_delete)

print("After:")
ut.print_linked_list(head)