from typing import List


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        # Greedy + Line Sweep + Binary Search: O(n * log(n + r)) time,
        # O(n) space

        n = len(stations)
        power_delta = [0] * n
        for i, station in enumerate(stations):
            start_index = max(0, i - r)
            power_delta[start_index] += station
            end_index = i + r + 1
            if end_index < n:
                power_delta[end_index] -= station

        def is_possible_min_power(min_power: int) -> bool:
            cur_power = 0
            cur_k = k
            new_power_delta = power_delta.copy()
            for i in range(n):
                cur_power += new_power_delta[i]
                if cur_power < min_power:
                    missing_power = min_power - cur_power
                    if missing_power > cur_k:
                        return False
                    cur_k -= missing_power
                    cur_power += missing_power
                    end_index = i + 2 * r + 1
                    if end_index < n:
                        new_power_delta[end_index] -= missing_power
            return True

        low = min(stations)
        high = sum(stations) + k
        max_min_power = low
        while low <= high:
            min_power = (low + high) // 2
            if is_possible_min_power(min_power):
                max_min_power = min_power
                low = min_power + 1
            else:
                high = min_power - 1
        return max_min_power
