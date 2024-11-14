from math import ceil


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        min_x = 0
        low = 1
        high = max(quantities)
        while low <= high:
            mid = low + (high - low) // 2
            stores = 0
            x = mid
            for quantity in quantities:
                x = max(x, mid)
                stores += ceil(quantity / mid)
            if stores <= n:
                min_x = x
                high = mid - 1
            else:
                low = mid + 1
        return min_x
