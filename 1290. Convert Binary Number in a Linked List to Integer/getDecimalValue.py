from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        # Math: O(n) time, O(1) space, where n is the size of
        # the linked list rooted at head

        decimal_value = 0
        cur_node = head
        while cur_node:
            decimal_value = decimal_value << 1 | cur_node.val
            cur_node = cur_node.next
        return decimal_value
