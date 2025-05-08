from typing import List
from heapq import heappop, heappush


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # Dijkstra's Algorithm: O(n * mlog(m * n)) time, O(m * n) space

        n = len(moveTime)
        m = len(moveTime[0])
        p_queue = [(0, 0, 0, 0)]
        min_time = [[float("inf")] * m for _ in range(n)]
        min_time[0][0] = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while p_queue:
            cur_time, time_delta, x, y = heappop(p_queue)
            if x == n - 1 and y == m - 1:
                break
            elif cur_time > min_time[x][y]:
                continue
            for dx, dy in directions:
                x2 = x + dx
                y2 = y + dy
                if time_delta == 1:
                    new_time_delta = 2
                else:
                    new_time_delta = 1
                if (
                    0 <= x2 < n
                    and 0 <= y2 < m
                    and max(moveTime[x2][y2], cur_time) + new_time_delta
                    < min_time[x2][y2]
                ):
                    min_time[x2][y2] = max(moveTime[x2][y2], cur_time) + new_time_delta
                    heappush(p_queue, (min_time[x2][y2], new_time_delta, x2, y2))
        return min_time[n - 1][m - 1]
