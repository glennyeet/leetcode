from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # DFS: O(m * n) time, O(m * n) space

        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = (
            ((0, 1), (0, -1)),
            ((1, 0), (-1, 0)),
            ((1, 0), (0, -1)),
            ((0, 1), (1, 0)),
            ((0, -1), (-1, 0)),
            ((0, 1), (-1, 0)),
        )
        top_connections = (2, 3, 4)
        right_connections = (1, 3, 5)
        bottom_connections = (2, 5, 6)
        left_connections = (1, 4, 6)

        def has_valid_path(cur_i: int, cur_j: int) -> bool:
            visited[cur_i][cur_j] = True
            if cur_i == m - 1 and cur_j == n - 1:
                return True
            for di, dj in directions[grid[cur_i][cur_j] - 1]:
                new_i = cur_i + di
                new_j = cur_j + dj
                if 0 <= new_i < m and 0 <= new_j < n and not visited[new_i][new_j]:
                    if (
                        di == -1
                        and dj == 0
                        and grid[new_i][new_j] in top_connections
                        or di == 0
                        and dj == 1
                        and grid[new_i][new_j] in right_connections
                        or di == 1
                        and dj == 0
                        and grid[new_i][new_j] in bottom_connections
                        or di == 0
                        and dj == -1
                        and grid[new_i][new_j] in left_connections
                    ):
                        if has_valid_path(new_i, new_j):
                            return True
            return False

        return has_valid_path(0, 0)
