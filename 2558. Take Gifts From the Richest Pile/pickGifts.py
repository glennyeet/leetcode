from heapq import heappushpop, heappush
from math import floor, sqrt


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        p_queue = []
        for pile in gifts:
            heappush(p_queue, -pile)
        for _ in range(1, k + 1):
            heappushpop(p_queue, -floor(sqrt(-p_queue[0])))
        return -sum(p_queue)
