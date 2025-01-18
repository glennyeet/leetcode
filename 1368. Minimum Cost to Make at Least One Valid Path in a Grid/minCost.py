from collections import deque
from math import inf


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # 0/1 BFS: O(m * n) time, O(m * n) space

        m = len(grid)
        n = len(grid[0])
        directions = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        queue = deque([(0, 0, 0)])
        min_cost = {(0, 0): 0}
        while queue:
            x, y, cost = queue.popleft()
            if x == m - 1 and y == n - 1:
                return cost
            for direction in directions:
                dx, dy = directions[direction]
                x2 = x + dx
                y2 = y + dy
                if direction == grid[x][y]:
                    new_cost = cost
                else:
                    new_cost = cost + 1
                if (
                    0 <= x2 < m
                    and 0 <= y2 < n
                    and new_cost < min_cost.get((x2, y2), inf)
                ):
                    min_cost[(x2, y2)] = new_cost
                    if direction == grid[x][y]:
                        queue.appendleft((x2, y2, new_cost))
                    else:
                        queue.append((x2, y2, new_cost))
        return min_cost[(m - 1, n - 1)]
