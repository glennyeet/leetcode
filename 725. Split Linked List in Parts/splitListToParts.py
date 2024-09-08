# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        total_nodes = 0
        node = head
        while node:
            total_nodes += 1
            node = node.next
        subset_len = total_nodes // k
        remainder = total_nodes % k
        node = head
        parts = []
        while node:
            subset = None
            subset_pointer = None
            for _ in range(subset_len):
                if not subset:
                    subset = ListNode(node.val)
                    subset_pointer = subset
                else:
                    subset_pointer.next = ListNode(node.val)
                    subset_pointer = subset_pointer.next
                node = node.next
            if remainder > 0:
                if not subset:
                    subset = ListNode(node.val)
                else:
                    subset_pointer.next = ListNode(node.val)
                node = node.next
                remainder -= 1
            parts.append(subset)
        parts_len = len(parts)
        if parts_len < k:
            remaining_subsets = k - parts_len
            for _ in range(remaining_subsets):
                parts.append(None)
        return parts
