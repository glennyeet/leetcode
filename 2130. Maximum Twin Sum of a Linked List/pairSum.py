from typing import Optional


# Definition for singly-linked list.\
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Linked List: O(n) time, O(n) space

        vals = []
        cur_node = head
        while cur_node:
            vals.append(cur_node.val)
            cur_node = cur_node.next
        n = len(vals)
        max_twin_sum = 0
        for i in range(n // 2):
            max_twin_sum = max(max_twin_sum, vals[i] + vals[n - 1 - i])
        return max_twin_sum
