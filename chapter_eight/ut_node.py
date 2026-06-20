# helper for chapter_eight
#chapter_eight/ut_node.py
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def find_node(head, target_value):
    current = head

    while current:
        if current.val == target_value:
            return current

        current = current.next

    return None


def print_linked_list(head):
    current = head

    while current:
        print(current.val, end="")

        if current.next:
            print(" -> ", end="")

        current = current.next
    print()