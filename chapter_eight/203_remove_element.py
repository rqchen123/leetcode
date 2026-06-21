import ut_node as ut
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        temp = dummy
        breakpoint()
        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            temp = temp.next
        return dummy.next


# Build: 4 -> 5 -> 1 -> 9
head = ut.build_linked_list([4, 5, 1, 9])

print("Before:")
ut.print_linked_list(head)

# Find the actual node object containing 5
node_to_delete = ut.find_node(head, 5)
print("node_to_delte:", node_to_delete)

solution = Solution()
head = solution.removeElements(head=head, val=5)

print("After:")
ut.print_linked_list(head)