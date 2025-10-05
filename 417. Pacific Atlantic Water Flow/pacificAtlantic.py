from typing import List
from heapq import heappush, heappop


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Priority Queue + BFS: O((m * n)log(m * n)) time, O(m * n) space

        m = len(heights)
        n = len(heights[0])
        flows_into_pacific = [[False] * n for _ in range(m)]
        pacific_priority_queue = []
        for c in range(n):
            flows_into_pacific[0][c] = True
            heappush(pacific_priority_queue, (heights[0][c], 0, c))
        for r in range(1, m):
            flows_into_pacific[r][0] = True
            heappush(pacific_priority_queue, (heights[r][0], r, 0))
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while pacific_priority_queue:
            height, r, c = heappop(pacific_priority_queue)
            for dr, dc in directions:
                r2 = r + dr
                c2 = c + dc
                if (
                    0 <= r2 < m
                    and 0 <= c2 < n
                    and heights[r2][c2] >= height
                    and not flows_into_pacific[r2][c2]
                ):
                    flows_into_pacific[r2][c2] = True
                    heappush(pacific_priority_queue, (heights[r2][c2], r2, c2))
        result = []
        flows_into_atlantic = [[False] * n for _ in range(m)]
        atlantic_priority_queue = []
        for c in range(n):
            flows_into_atlantic[m - 1][c] = True
            heappush(atlantic_priority_queue, (heights[m - 1][c], m - 1, c))
        for r in range(m - 1):
            flows_into_atlantic[r][n - 1] = True
            heappush(atlantic_priority_queue, (heights[r][n - 1], r, n - 1))
        while atlantic_priority_queue:
            height, r, c = heappop(atlantic_priority_queue)
            if flows_into_pacific[r][c]:
                result.append([r, c])
            for dr, dc in directions:
                r2 = r + dr
                c2 = c + dc
                if (
                    0 <= r2 < m
                    and 0 <= c2 < n
                    and heights[r2][c2] >= height
                    and not flows_into_atlantic[r2][c2]
                ):
                    flows_into_atlantic[r2][c2] = True
                    heappush(atlantic_priority_queue, (heights[r2][c2], r2, c2))
        return result
