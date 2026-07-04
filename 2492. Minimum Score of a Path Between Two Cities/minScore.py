from collections import defaultdict, deque
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # BFS: O(r + n) time, O(r + n) space, where r is the
        # size of roads

        adj_list = defaultdict(list)
        min_score = 0
        for a, b, distance in roads:
            adj_list[a].append((b, distance))
            adj_list[b].append((a, distance))
            min_score = max(min_score, distance)
        queue = deque([1])
        visited = set()
        while queue:
            a = queue.popleft()
            for b, distance in adj_list[a]:
                min_score = min(min_score, distance)
                if b not in visited:
                    queue.append(b)
                    visited.add(b)
        return min_score
