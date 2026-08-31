from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # Linked List: O(n) time, O(1) space, where n is the size of the linked
        # list head

        cur_node = head
        i = 1
        first_critical_point = -1
        last_critical_point = -1
        min_distance = float("inf")
        max_distance = -1
        while cur_node.next.next:
            left_node = cur_node.val
            middle_node = cur_node.next.val
            right_node = cur_node.next.next.val
            if (
                left_node < middle_node
                and middle_node > right_node
                or left_node > middle_node
                and middle_node < right_node
            ):
                if first_critical_point == -1:
                    first_critical_point = i
                elif i != first_critical_point:
                    min_distance = min(min_distance, i - last_critical_point)
                last_critical_point = i
            cur_node = cur_node.next
            i += 1
        if last_critical_point != first_critical_point:
            max_distance = last_critical_point - first_critical_point
        if min_distance == float("inf"):
            min_distance = -1
        return [min_distance, max_distance]
