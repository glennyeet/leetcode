from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # Binary search: O(nlog(m)) time, O(1) space, where
        # n is the size of candies, m is max(candies)

        left = 0
        right = max(candies)

        def can_allocate_candies(sub_pile_amount: int) -> bool:
            sub_piles = 0
            for pile in candies:
                sub_piles += pile // sub_pile_amount
            if sub_piles < k:
                return False
            return True

        while left < right:
            mid = (left + right + 1) // 2
            if can_allocate_candies(mid):
                left = mid
            else:
                right = mid - 1
        return left
