from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        # Math + Greedy: O(m * log(m) + n * log(n)) time, O(m + n) time,
        # where m is the max factor and n is the size of items

        max_factor = 0
        min_price = float("inf")
        for factor, price in items:
            max_factor = max(max_factor, factor)
            min_price = min(min_price, price)
        max_factor += 1
        factors_count = [0] * max_factor
        for factor, _ in items:
            factors_count[factor] += 1
        multiples_count = [0] * max_factor
        divisor = 1
        while divisor < max_factor:
            j = divisor
            while j < max_factor:
                multiples_count[divisor] += factors_count[j]
                j += divisor
            divisor += 1
        eligible_items = []
        for factor, price in items:
            if price <= min_price * 2:
                eligible_items.append((price, multiples_count[factor] - 1))
        eligible_items.sort()
        max_total_items = 0
        for price, bonus_items in eligible_items:
            afford = budget // price
            afford = min(afford, bonus_items)
            max_total_items += afford * 2
            budget -= afford * price
        afford = budget // min_price
        max_total_items += afford
        return max_total_items
