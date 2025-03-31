from typing import List
from heapq import heapify, heappop


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # Priority queue: O(nlog(n)) time, O(n) space

        n = len(weights)
        cut_scores = []
        for i in range(n - 1):
            cut_scores.append(weights[i] + weights[i + 1])
        max_priority_queue = []
        for score in cut_scores:
            max_priority_queue.append(-score)
        heapify(max_priority_queue)
        min_priority_queue = cut_scores
        heapify(min_priority_queue)
        max_score = weights[0] + weights[n - 1]
        min_score = weights[0] + weights[n - 1]
        for _ in range(k - 1):
            max_score += -heappop(max_priority_queue)
            min_score += heappop(min_priority_queue)
        return max_score - min_score
