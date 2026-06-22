import ut_node as ut
from typing import Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        temp = dummy
        breakpoint()
        for _ in range(left - 1):
            temp = temp.next

        previous = None
        current = temp.next
        for _ in range(right-left +1):
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        print('reverse:')
        ut.print_linked_list(previous)

        print("temp:")
        ut.print_linked_list(temp)
        tail = temp.next
        temp.next = previous
        tail.next = current
        return dummy.next





head = ut.build_linked_list([1, 2, 3, 4, 5])

print("Before:")
ut.print_linked_list(head)

solution = Solution()
head = solution.reverseBetween(head=head, left=2, right=4)

print("After:")
ut.print_linked_list(head)