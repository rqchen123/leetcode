import ut_node as ut

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNode(self, head, node):
        dummy = ListNode(0, head)
        current = dummy
        breakpoint()
        while current.next:
            if current.next == node:
                current.next=current.next.next
                break
            current = current.next

        return dummy.next

# Build: 4 -> 5 -> 1 -> 9
head = ut.build_linked_list([4, 5, 1, 9])

print("Before:")
ut.print_linked_list(head)

# Find the actual node object containing 5
node_to_delete = ut.find_node(head, 5)
print("node_to_delte:", node_to_delete)

solution = Solution()
head = solution.deleteNode(head, node_to_delete)

print("After:")
ut.print_linked_list(head)