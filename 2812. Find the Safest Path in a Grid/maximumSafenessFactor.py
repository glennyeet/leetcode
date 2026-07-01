from collections import deque
from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # BFS + Binary Search: O(n^2 + n^2 * log(n)) time, O(n^2) space

        n = len(grid)
        safeness_factor = [[float("inf")] * n for _ in range(n)]
        grid_queue = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    grid_queue.append((r, c))
                    safeness_factor[r][c] = 0
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while grid_queue:
            r, c = grid_queue.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (
                    0 <= nr < n
                    and 0 <= nc < n
                    and safeness_factor[nr][nc] > safeness_factor[r][c] + 1
                ):
                    safeness_factor[nr][nc] = safeness_factor[r][c] + 1
                    grid_queue.append((nr, nc))

        def is_path(min_safeness_factor: int) -> bool:
            path_queue = deque()
            visited = [[False] * n for _ in range(n)]
            if safeness_factor[0][0] >= min_safeness_factor:
                path_queue.append((0, 0))
                visited[0][0] = True
            while path_queue:
                r, c = path_queue.popleft()
                if (r, c) == (n - 1, n - 1):
                    return True
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (
                        0 <= nr < n
                        and 0 <= nc < n
                        and not visited[nr][nc]
                        and safeness_factor[nr][nc] >= min_safeness_factor
                    ):
                        visited[nr][nc] = True
                        path_queue.append((nr, nc))
            return False

        left = 0
        right = n
        while left < right:
            mid = (left + right + 1) // 2
            if is_path(mid):
                left = mid
            else:
                right = mid - 1
        return left
