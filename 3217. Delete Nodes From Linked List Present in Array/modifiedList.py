# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Dict
        nums_dict = defaultdict(bool)
        node = head
        while node is not None:
            nums_dict[node.val] = False
            node = node.next
        for num in nums:
            nums_dict[num] = True
        node = head
        prev_node = None
        while node is not None:
            if nums_dict[node.val]:
                if node.val == head.val:
                    head = node.next
                elif node.next == None:
                    prev_node.next = None
                else:
                    prev_node.next = node.next
            else:
                prev_node = node
            node = node.next
        return head

        # Set
        # dummy_node = ListNode(next=head)
        # curr_node = dummy_node
        # nums_set = set(nums)
        # while curr_node.next:
        #     if curr_node.next.val in nums_set:
        #         curr_node.next = curr_node.next.next
        #     else:
        #         curr_node = curr_node.next
        # return dummy_node.next