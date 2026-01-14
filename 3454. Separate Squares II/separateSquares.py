from typing import List


class SegmentTree:
    def __init__(self, x_list: list[int]) -> None:
        self.x_list = x_list
        self.n = len(x_list) - 1
        self.cover_count = [0] * (4 * self.n)
        self.covered_length = [0] * (4 * self.n)

    def update(
        self,
        new_left: int,
        new_right: int,
        new_val: int,
        cur_left: int,
        cur_right: int,
        cur_pos: int,
    ) -> None:
        if self.x_list[cur_right + 1] <= new_left or self.x_list[cur_left] >= new_right:
            return
        elif (
            new_left <= self.x_list[cur_left]
            and self.x_list[cur_right + 1] <= new_right
        ):
            self.cover_count[cur_pos] += new_val
        else:
            mid = (cur_left + cur_right) // 2
            self.update(new_left, new_right, new_val, cur_left, mid, cur_pos * 2 + 1)
            self.update(
                new_left, new_right, new_val, mid + 1, cur_right, cur_pos * 2 + 2
            )
        if self.cover_count[cur_pos] > 0:
            self.covered_length[cur_pos] = (
                self.x_list[cur_right + 1] - self.x_list[cur_left]
            )
        else:
            if cur_left == cur_right:
                self.covered_length[cur_pos] = 0
            else:
                self.covered_length[cur_pos] = (
                    self.covered_length[cur_pos * 2 + 1]
                    + self.covered_length[cur_pos * 2 + 2]
                )

    def query(self) -> int:
        return self.covered_length[0]


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # Line Sweep + Segment Tree: O(n * log(n)) time, O(n) space, where
        # n is the size of squares

        events = []
        x_set = set()
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
            x_set.update((x, x + l))
        events.sort()
        x_list = sorted(x_set)
        segment_tree = SegmentTree(x_list)
        total_area = 0.0
        prev_y = events[0][0]
        for y, val, x_left, x_right in events:
            total_area += segment_tree.query() * (y - prev_y)
            segment_tree.update(x_left, x_right, val, 0, segment_tree.n - 1, 0)
            prev_y = y
        segment_tree = SegmentTree(x_list)
        cur_area = 0.0
        prev_y = events[0][0]
        for y, val, x_left, x_right in events:
            combined_width = segment_tree.query()
            if cur_area + combined_width * (y - prev_y) >= total_area / 2.0:
                return prev_y + (total_area / 2.0 - cur_area) / combined_width
            cur_area += combined_width * (y - prev_y)
            segment_tree.update(x_left, x_right, val, 0, segment_tree.n - 1, 0)
            prev_y = y
        return prev_y + (total_area / 2.0 - cur_area) / combined_width
