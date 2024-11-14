from math import ceil


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        min_x = 0
        low = 1
        high = max(quantities)
        while low <= high:
            x = low + (high - low) // 2
            stores = 0
            for quantity in quantities:
                stores += ceil(quantity / x)
            if stores <= n:
                min_x = x
                high = x - 1
            else:
                low = x + 1
        return min_x
