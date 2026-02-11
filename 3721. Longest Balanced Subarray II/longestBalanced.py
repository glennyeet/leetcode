from typing import List


class SegmentTree:
    def __init__(self, nums: list[int]) -> None:
        self.n = len(nums)
        self.min_num = [0] * (4 * self.n)
        self.max_num = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1, nums)

    def build(self, node: int, left: int, right: int, nums: list[int]) -> None:
        if left == right:
            self.min_num[node] = nums[left]
            return
        mid = (left + right) // 2
        self.build(node * 2, left, mid, nums)
        self.build(node * 2 + 1, mid + 1, right, nums)
        self.pull(node)

    def pull(self, node: int) -> None:
        self.min_num[node] = min(self.min_num[node * 2], self.min_num[node * 2 + 1])
        self.max_num[node] = max(self.max_num[node * 2], self.max_num[node * 2 + 1])

    def apply(self, node: int, num: int) -> None:
        self.min_num[node] += num
        self.max_num[node] += num
        self.lazy[node] += num

    def push(self, node: int) -> None:
        if self.lazy[node] != 0:
            self.apply(node * 2, self.lazy[node])
            self.apply(node * 2 + 1, self.lazy[node])
            self.lazy[node] = 0

    def range_add(
        self,
        query_left: int,
        query_right: int,
        num: int,
        node=1,
        left=0,
        right: int | None = None,
    ) -> None:
        if right is None:
            right = self.n - 1
        elif query_right < left or query_left > right:
            return
        elif query_left <= left and right <= query_right:
            self.apply(node, num)
            return
        self.push(node)
        mid = (left + right) // 2
        self.range_add(query_left, query_right, num, node * 2, left, mid)
        self.range_add(query_left, query_right, num, node * 2 + 1, mid + 1, right)
        self.pull(node)

    def walk(
        self,
        query_left: int,
        query_right: int,
        node=1,
        left=0,
        right: int | None = None,
        target: int | None = None,
    ) -> int | float | None:
        if right is None:
            right = self.n - 1
        elif query_right < left or query_left > right:
            return float("inf")
        elif target < self.min_num[node] or target > self.max_num[node]:
            return float("inf")
        elif query_left == query_right:
            return left
        self.push(node)
        mid = (left + right) // 2
        if self.min_num[node * 2] <= target <= self.max_num[node * 2]:
            return self.walk(
                query_left, min(query_right, mid), node * 2, left, mid, target
            )
        else:
            return self.walk(
                max(query_left, mid + 1),
                query_right,
                node * 2 + 1,
                mid + 1,
                right,
                target,
            )

    def get(self, index: int, node=1, left=0, right: int | None = None) -> int:
        if right is None:
            right = self.n - 1
        elif left == right:
            return self.min_num[node]
        self.push(node)
        mid = (left + right) // 2
        if index <= mid:
            return self.get(index, node * 2, left, mid)
        else:
            return self.get(index, node * 2 + 1, mid + 1, right)


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        # Segment Tree + Prefix Sum: O(n * log(n)) time, O(n) space

        n = len(nums)
        segment_tree = SegmentTree([0] * n)
        cur_node = 0
        last_index = {}
        max_length = 0
        for i, num in enumerate(nums):
            delta = 1
            if num % 2 == 1:
                delta = -delta
            if num in last_index:
                segment_tree.range_add(last_index[num], i - 1, -delta)
            last_index[num] = i
            if i > 0:
                cur_node = segment_tree.get(i - 1)
            cur_node += delta
            if cur_node == 0:
                max_length = max(max_length, i + 1)
            else:
                prev_node = segment_tree.walk(0, i - 1, 1, 0, n - 1, cur_node)
                max_length = max(max_length, i - prev_node)
            segment_tree.range_add(i, i, cur_node)
        return max_length
