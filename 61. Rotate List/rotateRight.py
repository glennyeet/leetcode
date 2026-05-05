from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Linked List: O(n) time, O(1) space, where n is the size of the linked
        # list rooted at head

        total_nodes = 0
        cur = ListNode(next=head)
        while cur.next:
            total_nodes += 1
            cur = cur.next
        if total_nodes == 0:
            return None
        cutoff = k % total_nodes
        if cutoff == 0:
            return head
        cutoff = total_nodes - cutoff
        old_head = ListNode(next=head)
        new_tail = old_head
        for _ in range(cutoff):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        old_tail = new_head
        while old_tail.next:
            old_tail = old_tail.next
        old_tail.next = old_head.next
        return new_head
