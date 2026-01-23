from typing import List
from sortedcontainers import SortedList


class Node:
    def __init__(self, index: int, num: int) -> None:
        self.index = index
        self.num = num
        self.prev: Node = None
        self.next: Node = None


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # Doubly Linked List + Hash Table + B-tree: O(n * log(n)) time, O(n) space,
        # where n is the size of nums

        root = Node(-1, float("-inf"))
        curr = root
        min_operations = 0
        total_out_of_order = 0
        index_to_node: dict[int, Node] = {}
        for i, num in enumerate(nums):
            curr.next = Node(i, num)
            curr.next.prev = curr
            if curr.num > curr.next.num:
                total_out_of_order += 1
            curr = curr.next
            index_to_node[i] = curr
        sorted_list = SortedList()
        curr = root.next
        while curr.next:
            sorted_list.add((curr.num + curr.next.num, curr.index, curr.next.index))
            curr = curr.next
        while total_out_of_order > 0:
            pair_sum, left_index, right_index = sorted_list[0]
            sorted_list.remove((pair_sum, left_index, right_index))
            left_node = index_to_node[left_index]
            right_node = index_to_node[right_index]
            if left_node.num > right_node.num:
                total_out_of_order -= 1
            if left_node.prev != root and left_node.prev.num > left_node.num:
                total_out_of_order -= 1
            if right_node.next and right_node.num > right_node.next.num:
                total_out_of_order -= 1
            if right_node.next:
                sorted_list.remove(
                    (
                        right_node.num + right_node.next.num,
                        right_node.index,
                        right_node.next.index,
                    )
                )
            prev_num = left_node.num
            left_node.num += right_node.num
            left_node.next = right_node.next
            if right_node.next:
                right_node.next.prev = left_node
                sorted_list.add(
                    (
                        left_node.num + left_node.next.num,
                        left_node.index,
                        left_node.next.index,
                    )
                )
            if left_node.prev != root:
                sorted_list.remove(
                    (
                        left_node.prev.num + prev_num,
                        left_node.prev.index,
                        left_node.index,
                    )
                )
                sorted_list.add(
                    (
                        left_node.prev.num + left_node.num,
                        left_node.prev.index,
                        left_node.index,
                    )
                )
            if left_node.prev != root and left_node.prev.num > left_node.num:
                total_out_of_order += 1
            if left_node.next and left_node.num > left_node.next.num:
                total_out_of_order += 1
            min_operations += 1
        return min_operations
