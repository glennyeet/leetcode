from typing import List
from collections import deque
from heapq import heappop, heappush


class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        # Queue + Dijkstra's Algorithm: O(m * n * k * log(m * n)) time,
        # O(m * n * k) space

        m = len(grid)
        n = len(grid[0])
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], i, j))
        cells.sort()
        queues = [deque(cells) for _ in range(k + 1)]
        min_cost = [[[float("inf")] * (k + 1) for _ in range(n)] for _ in range(m)]
        min_cost[0][0][k] = 0
        priority_queue = [(0, 0, 0, k)]
        directions = [(1, 0), (0, 1)]
        while priority_queue:
            cur_cost, x, y, k_left = heappop(priority_queue)
            if cur_cost > min_cost[x][y][k_left]:
                continue
            elif x == m - 1 and y == n - 1:
                return cur_cost
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = cur_cost + grid[nx][ny]
                    if new_cost < min_cost[nx][ny][k_left]:
                        min_cost[nx][ny][k_left] = new_cost
                        heappush(priority_queue, (new_cost, nx, ny, k_left))
            if k_left > 0:
                while len(queues[k_left]) > 0 and queues[k_left][0][0] <= grid[x][y]:
                    _, nx, ny = queues[k_left].popleft()
                    new_k_left = k_left - 1
                    if min_cost[nx][ny][new_k_left] > min_cost[x][y][k_left]:
                        min_cost[nx][ny][new_k_left] = min_cost[x][y][k_left]
                        for i in range(k_left - 2, -1, -1):
                            min_cost[nx][ny][i] = min_cost[x][y][k_left]
                        heappush(
                            priority_queue,
                            (min_cost[nx][ny][new_k_left], nx, ny, new_k_left),
                        )
        return -1
