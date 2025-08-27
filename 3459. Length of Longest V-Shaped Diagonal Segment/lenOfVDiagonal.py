from typing import List
from functools import cache


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        # Top-down DP: O(n * m) time, O(n * m) space

        n = len(grid)
        m = len(grid[0])
        directions = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

        @cache
        def find_longest_segment(
            cur_i: int, cur_j: int, cur_direction: int, turn_made: bool
        ) -> int:
            longest_segment = 1
            cur_value = grid[cur_i][cur_j]
            if cur_value == 1:
                new_value = 2
            else:
                new_value = 2 - cur_value
            di, dj = directions[cur_direction]
            new_i = cur_i + di
            new_j = cur_j + dj
            if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] == new_value:
                longest_segment = max(
                    longest_segment,
                    1 + find_longest_segment(new_i, new_j, cur_direction, turn_made),
                )
            if not turn_made:
                new_direction = (cur_direction + 1) % 4
                di, dj = directions[new_direction]
                new_i = cur_i + di
                new_j = cur_j + dj
                if (
                    0 <= new_i < n
                    and 0 <= new_j < m
                    and grid[new_i][new_j] == new_value
                ):
                    longest_segment = max(
                        longest_segment,
                        1 + find_longest_segment(new_i, new_j, new_direction, True),
                    )
            return longest_segment

        longest_segment = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for direction in range(4):
                        longest_segment = max(
                            longest_segment,
                            find_longest_segment(i, j, direction, False),
                        )
        return longest_segment
