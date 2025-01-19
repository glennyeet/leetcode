from heapq import heapify, heappop, heappush


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # BFS + Priority Queue: O(m * nlog(m * n)) time, O(m * n) space

        m = len(heightMap)
        n = len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        priority_queue = []
        for i in range(m):
            priority_queue.append((heightMap[i][0], (i, 0)))
            visited[i][0] = True
            priority_queue.append((heightMap[i][n - 1], (i, n - 1)))
            visited[i][n - 1] = True
        for j in range(1, n - 1):
            priority_queue.append((heightMap[0][j], (0, j)))
            visited[0][j] = True
            priority_queue.append((heightMap[m - 1][j], (m - 1, j)))
            visited[m - 1][j] = True
        heapify(priority_queue)
        min_boundary_height = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        volume = 0
        while priority_queue:
            height, (x, y) = heappop(priority_queue)
            min_boundary_height = max(min_boundary_height, height)
            for dx, dy in directions:
                x2 = x + dx
                y2 = y + dy
                if 0 <= x2 < m and 0 <= y2 < n and not visited[x2][y2]:
                    visited[x2][y2] = True
                    height2 = heightMap[x2][y2]
                    heappush(priority_queue, (height2, (x2, y2)))
                    if height2 < min_boundary_height:
                        volume += min_boundary_height - height2
        return volume
