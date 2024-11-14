from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = 0
        low = 1
        high = max(piles)
        while low <= high:
            k = low + (high - low) // 2
            hours = 0
            for pile in piles:
                hours += ceil(pile / k)
            if hours <= h:
                min_k = k
                high = k - 1
            else:
                low = k + 1
        return min_k
