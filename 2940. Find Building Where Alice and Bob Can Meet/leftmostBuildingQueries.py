from collections import defaultdict, deque

# from bisect import bisect_right
from heapq import heappop, heappush


class Solution:
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        # Monotonic stack: O(qlog(h)) time, O(q + h) space

        # query_lookup = defaultdict(list)
        # for i, [a, b] in enumerate(queries):
        #     query_lookup[max(a, b)].append((i, min(a, b)))
        # stack = deque()
        # ans = [-1] * len(queries)
        # for b in range(len(heights) - 1, -1, -1):
        #     while stack and stack[0][1] <= heights[b]:
        #         stack.popleft()
        #     stack.appendleft((b, heights[b]))
        #     for i, a in query_lookup[b]:
        #         max_pair_height = max(heights[a], heights[b])
        #         if a == b or heights[a] < heights[b]:
        #             ans[i] = b
        #         else:
        #             stack_building = bisect_right(
        #                 stack,
        #                 max_pair_height,
        #                 key=lambda b: b[1],
        #             )
        #             if stack_building < len(stack):
        #                 ans[i] = stack[stack_building][0]
        # return ans

        # Priority queue: O(qlog(q)) time, O(q + h) space

        query_lookup = defaultdict(list)
        for i, [a, b] in enumerate(queries):
            query_lookup[max(a, b)].append((i, min(a, b)))
        p_queue = []
        ans = [-1] * len(queries)
        for b, height_b in enumerate(heights):
            while p_queue and p_queue[0][0] < height_b:
                _, query_i = heappop(p_queue)
                ans[query_i] = b
            for i, a in query_lookup[b]:
                height_a = heights[a]
                if a == b or height_a < height_b:
                    ans[i] = b
                else:
                    heappush(p_queue, (max(height_a, height_b), i))
        return ans
