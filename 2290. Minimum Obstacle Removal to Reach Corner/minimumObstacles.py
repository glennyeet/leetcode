from collections import defaultdict
from math import inf
from heapq import heappop, heappush


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        adj_list = defaultdict(lambda: defaultdict(int))
        m = len(grid)
        n = len(grid[0])
        for x in range(m):
            for y in range(n):
                if x - 1 >= 0:
                    adj_list[(x, y)][(x - 1, y)] = grid[x - 1][y]
                if x + 1 < m:
                    adj_list[(x, y)][(x + 1, y)] = grid[x + 1][y]
                if y - 1 >= 0:
                    adj_list[(x, y)][(x, y - 1)] = grid[x][y - 1]
                if y + 1 < n:
                    adj_list[(x, y)][(x, y + 1)] = grid[x][y + 1]
        total_obstacles = [[inf] * n for _ in range(m)]
        total_obstacles[0][0] = 0
        visited = set()
        p_queue = [(0, (0, 0))]
        while p_queue:
            u_obstacles, (u_x, u_y) = heappop(p_queue)
            if (u_x, u_y) == (m - 1, n - 1):
                return u_obstacles
            elif (u_x, u_y) in visited:
                continue
            visited.add((u_x, u_y))
            for (v_x, v_y), is_obstacle in adj_list[(u_x, u_y)].items():
                new_obstacles = u_obstacles + is_obstacle
                if new_obstacles < total_obstacles[v_x][v_y]:
                    total_obstacles[v_x][v_y] = new_obstacles
                    heappush(p_queue, (new_obstacles, (v_x, v_y)))
