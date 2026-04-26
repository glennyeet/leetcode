from typing import List


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # DFS: O(m * n) time, O(m * n) space

        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def is_cycle(cur_i: int, cur_j: int, parent_i: int, parent_j: int) -> bool:
            visited[cur_i][cur_j] = True
            for di, dj in directions:
                new_i = cur_i + di
                new_j = cur_j + dj
                if (
                    0 <= new_i < m
                    and 0 <= new_j < n
                    and grid[new_i][new_j] == grid[cur_i][cur_j]
                ):
                    if not visited[new_i][new_j]:
                        if is_cycle(new_i, new_j, cur_i, cur_j):
                            return True
                    elif (new_i, new_j) != (parent_i, parent_j):
                        return True
            return False

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if is_cycle(i, j, -1, -1):
                        return True
        return False
