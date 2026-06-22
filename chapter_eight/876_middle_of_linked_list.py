import ut_node as ut
from typing import Optional


#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


head = ut.build_linked_list([1, 1, 2])

print("Before:")
ut.print_linked_list(head)

solution = Solution()
head = solution.middleNode(head=head)

print("After:")
ut.print_linked_list(head)