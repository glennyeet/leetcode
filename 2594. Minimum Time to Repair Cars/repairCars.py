from typing import List
from math import floor, sqrt


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # Binary search: O(rlog(t)) time, O(1) space, where
        # r is the size of ranks and
        # t = max(ranks) * cars^2 - min(ranks) + 1

        left = min(ranks)
        right = max(ranks) * cars**2

        def is_repair_time_possible(time: int) -> bool:
            repaired_cars = 0
            for rank in ranks:
                repaired_cars += floor(sqrt(time // rank))
            return repaired_cars >= cars

        while left < right:
            mid = (left + right) // 2
            if is_repair_time_possible(mid):
                right = mid
            else:
                left = mid + 1
        return left
