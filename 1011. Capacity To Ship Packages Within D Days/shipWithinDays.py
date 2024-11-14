from math import ceil


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_capacity = 0
        low = max(weights)
        high = sum(weights)
        while low <= high:
            capacity = low + (high - low) // 2
            days_taken = 1
            total_weight = 0
            for weight in weights:
                if ceil((total_weight + weight) / capacity) > days_taken:
                    total_weight += capacity * days_taken - total_weight + weight
                    days_taken += 1
                else:
                    total_weight += weight
            if days_taken <= days:
                min_capacity = capacity
                high = capacity - 1
            else:
                low = capacity + 1
        return min_capacity
