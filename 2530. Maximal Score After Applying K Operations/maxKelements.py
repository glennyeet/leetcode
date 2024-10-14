from heapq import heapify, heappush, heappop
from math import ceil


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums_pq = []
        for num in nums:
            nums_pq.append(-num)
        heapify(nums_pq)
        max_score = 0
        for _ in range(k):
            num = -heappop(nums_pq)
            max_score += num
            heappush(nums_pq, -ceil(num / 3))
        return max_score
