import ut_node as ut
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self,
        headA: ListNode,
        headB: ListNode
    ) -> Optional[ListNode]:

        pointer_a, pointer_b = headA, headB

        while pointer_b != pointer_a:
            print(
                "A:",
                pointer_a.val if pointer_a else None,
                "B:",
                pointer_b.val if pointer_b else None
            )

            pointer_a = (
                headB if pointer_a is None else pointer_a.next
            )

            pointer_b = (
                headA if pointer_b is None else pointer_b.next
            )

        return pointer_a


common = ut.build_linked_list([8, 4, 5])

headA = ut.build_linked_list([4, 1])
headB = ut.build_linked_list([5, 6, 1])

# Both lists connect to the same common nodes
ut.connect_to_common(headA, common)
ut.connect_to_common(headB, common)

print("List A:")
ut.print_linked_list(headA)

print("List B:")
ut.print_linked_list(headB)

solution = Solution()

intersection = solution.getIntersectionNode(headA, headB)

if intersection:
    print("Intersection value:", intersection.val)
else:
    print("No intersection")