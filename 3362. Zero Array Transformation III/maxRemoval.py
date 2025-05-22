from typing import List
from heapq import heappush, heappop


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        # Greedy + Priority Queue: O(nlog(q)) time, O(q) space

        n = len(nums)
        q = len(queries)
        decrement_delta = [[] for _ in range(n + 1)]
        for i, (l, r) in enumerate(queries):
            decrement_delta[l].append((i, 1, r))
            decrement_delta[r + 1].append((i, -1, -1))
        priority_queue = []
        used_queries = [False] * q
        current_queries = set()
        for i in range(n):
            for query_index, decrement, r in decrement_delta[i]:
                if decrement == 1:
                    heappush(priority_queue, (-r, query_index))
                else:
                    if query_index in current_queries:
                        current_queries.remove(query_index)
            while nums[i] > len(current_queries):
                if len(priority_queue) == 0:
                    return -1
                r, query_index = heappop(priority_queue)
                r = -r
                if i > r:
                    continue
                current_queries.add(query_index)
                used_queries[query_index] = True
        return q - used_queries.count(True)
