# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# import math


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        def find_gcd(a: int, b: int) -> int:  # Binary GCD algorithm
            d = 0
            while a & 1 == 0 and b & 1 == 0:
                a >>= 1
                b >>= 1
                d += 1
            while a != b:
                if a > b:
                    a -= b
                    while a & 1 == 0:
                        a >>= 1
                else:
                    b -= a
                    while b & 1 == 0:
                        b >>= 1
            return 2**d * a

        dummy_node = ListNode(next=head)
        while dummy_node.next.next:
            dummy_node.next.next = ListNode(
                find_gcd(dummy_node.next.val, dummy_node.next.next.val),
                # math.gcd(dummy_node.next.val, dummy_node.next.next.val),
                dummy_node.next.next,
            )
            dummy_node = dummy_node.next.next
        return head
