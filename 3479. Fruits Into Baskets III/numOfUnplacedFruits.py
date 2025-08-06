from typing import List


class SegmentTree:
    def __init__(self, array: list[int]) -> None:
        self.n = len(array)
        self.array = array
        self.tree = [float("inf")] * (4 * self.n)
        self.build(1, 0, self.n - 1)

    def build(self, node: int, start: int, end: int) -> None:
        if start == end:
            self.tree[node] = self.array[start]
            return
        mid = (start + end) // 2
        left_child = 2 * node
        right_child = 2 * node + 1
        self.build(left_child, start, mid)
        self.build(right_child, mid + 1, end)
        self.tree[node] = max(self.tree[left_child], self.tree[right_child])

    def update(self, node: int, start: int, end: int, index: int, value: int) -> None:
        if start == end:
            self.array[start] = value
            self.tree[node] = value
            return
        mid = (start + end) // 2
        left_child = 2 * node
        right_child = 2 * node + 1
        if start <= index <= mid:
            self.update(left_child, start, mid, index, value)
        else:
            self.update(right_child, mid + 1, end, index, value)
        self.tree[node] = max(self.tree[left_child], self.tree[right_child])

    def query(self, node, start, end, value: int) -> int:
        if value > self.tree[node]:
            return -1
        if start == end:
            return start
        left_child = 2 * node
        right_child = 2 * node + 1
        mid = (start + end) // 2
        if self.tree[left_child] >= value:
            return self.query(left_child, start, mid, value)
        else:
            return self.query(right_child, mid + 1, end, value)


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # Segment Tree: O(nlog(n)) time, O(n) space

        n = len(fruits)
        segment_tree = SegmentTree(baskets)
        unplaced_fruits = 0
        for fruit in fruits:
            basket = segment_tree.query(1, 0, n - 1, fruit)
            if basket == -1:
                unplaced_fruits += 1
            else:
                segment_tree.update(1, 0, n - 1, basket, 0)
        return unplaced_fruits
