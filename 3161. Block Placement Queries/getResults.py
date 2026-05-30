from typing import List
from sortedcontainers import SortedList


class SegmentTree:
    def __init__(self, size: int, init_val: int):
        self.max_tree = [0] * ((size + 1) * 4)
        self.build(1, 0, size, init_val)

    def max(
        self,
        node: int,
        seg_left: int,
        seg_right: int,
        query_left: int,
        query_right: int,
    ) -> int:
        if query_left > query_right:
            return 0
        if query_left == seg_left and query_right == seg_right:
            return self.max_tree[node]
        seg_mid = (seg_left + seg_right) // 2
        return max(
            self.max(
                node * 2, seg_left, seg_mid, query_left, min(query_right, seg_mid)
            ),
            self.max(
                node * 2 + 1,
                seg_mid + 1,
                seg_right,
                max(query_left, seg_mid + 1),
                query_right,
            ),
        )

    def build(self, node: int, seg_left: int, seg_right: int, init_val: int) -> None:
        if seg_left == seg_right:
            self.max_tree[node] = init_val
        else:
            seg_mid = (seg_left + seg_right) // 2
            self.build(node * 2, seg_left, seg_mid, init_val)
            self.build(node * 2 + 1, seg_mid + 1, seg_right, init_val)
            self.max_tree[node] = max(
                self.max_tree[node * 2], self.max_tree[node * 2 + 1]
            )

    def update(
        self, node: int, seg_left: int, seg_right: int, pos: int, val: int
    ) -> None:
        if seg_left == seg_right:
            self.max_tree[node] = val
        else:
            seg_mid = (seg_left + seg_right) // 2
            if pos <= seg_mid:
                self.update(node * 2, seg_left, seg_mid, pos, val)
            else:
                self.update(node * 2 + 1, seg_mid + 1, seg_right, pos, val)
            self.max_tree[node] = max(
                self.max_tree[node * 2], self.max_tree[node * 2 + 1]
            )


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        # Segment Tree + Binary Search: O(q * (log(q) + log(m)))
        # time, O(q + m) space, where q is the size of queries
        # and m is max_coordinate

        max_coordinate = 0
        for query in queries:
            if query[0] == 2:
                max_coordinate = max(max_coordinate, query[1])
        max_coordinate += 1
        obstacles = SortedList()
        max_gap_tree = SegmentTree(max_coordinate, 0)
        obstacles.add(0)
        inf = 10**20
        obstacles.add(inf)
        max_gap_tree.update(1, 0, max_coordinate - 1, 0, inf)
        results = []
        for query in queries:
            if query[0] == 1:
                _, x = query
                right_obstacle_idx = obstacles.bisect_left(x)
                left_obstacle_idx = right_obstacle_idx - 1
                max_gap_tree.update(
                    1,
                    0,
                    max_coordinate - 1,
                    obstacles[left_obstacle_idx],
                    x - obstacles[left_obstacle_idx],
                )
                max_gap_tree.update(
                    1, 0, max_coordinate - 1, x, obstacles[right_obstacle_idx] - x
                )
                obstacles.add(x)
            else:
                _, x, sz = query
                right_obstacle_idx = obstacles.bisect_left(x)
                left_obstacle_idx = right_obstacle_idx - 1
                max_empty_block = max_gap_tree.max(
                    1, 0, max_coordinate - 1, 0, obstacles[left_obstacle_idx] - 1
                )
                max_empty_block = max(max_empty_block, x - obstacles[left_obstacle_idx])
                results.append(max_empty_block >= sz)
        return results
