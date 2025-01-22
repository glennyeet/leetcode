from collections import deque
from math import inf


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # BFS: O(m * n) time, O(m * n) space

        m = len(mat)
        n = len(mat[0])
        distances = [[inf] * n for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if not mat[i][j]:
                    distances[i][j] = 0
                    queue.append((i, j, 0))
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            x, y, distance = queue.popleft()
            for dx, dy in directions:
                x2 = x + dx
                y2 = y + dy
                if 0 <= x2 < m and 0 <= y2 < n and distances[x2][y2] == inf:
                    new_distance = distance + 1
                    distances[x2][y2] = new_distance
                    queue.append((x2, y2, new_distance))
        return distances
