from typing import List
from heapq import heappop, heappush


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # Dijkstra's Algorithm: O(n * m(log(n * m))) time, O(n * m) space

        n = len(moveTime)
        m = len(moveTime[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        p_queue = [(0, 0, 0)]
        min_time = [[float("inf")] * m for _ in range(n)]
        min_time[0][0] = 0
        while p_queue:
            seconds, x, y = heappop(p_queue)
            if x == n - 1 and y == m - 1:
                break
            elif seconds < min_time[x][y]:
                continue
            for dx, dy in directions:
                x2 = x + dx
                y2 = y + dy
                if (
                    0 <= x2 < n
                    and 0 <= y2 < m
                    and max(moveTime[x2][y2], seconds) + 1 < min_time[x2][y2]
                ):
                    min_time[x2][y2] = max(moveTime[x2][y2], seconds) + 1
                    heappush(p_queue, (min_time[x2][y2], x2, y2))
        return min_time[n - 1][m - 1]
