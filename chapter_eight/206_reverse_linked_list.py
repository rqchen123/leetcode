import ut_node as ut
from typing import Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        breakpoint()
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous

head = ut.build_linked_list([1, 2, 3, 4, 5])

print("Before:")
ut.print_linked_list(head)

solution = Solution()
head = solution.reverseList(head=head)

print("After:")
ut.print_linked_list(head)