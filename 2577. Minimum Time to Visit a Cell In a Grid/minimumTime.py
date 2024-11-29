from heapq import heappop, heappush
from math import inf


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        m = len(grid)
        n = len(grid[0])
        time = [[inf] * n for _ in range(m)]
        time[0][0] = 0
        p_queue = [(0, (0, 0))]
        while p_queue:
            u_time, (u_row, u_col) = heappop(p_queue)
            if (u_row, u_col) == (m - 1, n - 1):
                return u_time
            for dx, dy in directions:
                v_row = u_row + dx
                v_col = u_col + dy
                if 0 <= v_row < m and 0 <= v_col < n:
                    min_time = grid[v_row][v_col]
                    new_time = max(u_time + 1, min_time + (min_time - u_time - 1) % 2)
                    if new_time < time[v_row][v_col]:
                        time[v_row][v_col] = new_time
                        heappush(p_queue, (new_time, (v_row, v_col)))
