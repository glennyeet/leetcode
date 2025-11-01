from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Hash Table: O(n) time, O(n) space, where n is
        # the size of nums

        nums_set = set(nums)
        dummy_node = ListNode(next=head)
        cur_node = dummy_node
        while cur_node.next:
            if cur_node.next.val in nums_set:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
        return dummy_node.next
