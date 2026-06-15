from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        n = 0
        cur_node = head
        while cur_node:
            n += 1
            cur_node = cur_node.next
        mid = n // 2
        i = 0
        cur_node = ListNode(next=head)
        while cur_node.next:
            if i == mid:
                cur_node.next = cur_node.next.next
                break
            cur_node = cur_node.next
            i += 1
        return head
