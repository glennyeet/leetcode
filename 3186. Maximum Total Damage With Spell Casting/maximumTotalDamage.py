from typing import List
from collections import Counter


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # Hash Table + Sorting + Bottom-up DP: O(p * log(p)) time,
        # O(p) space, where p is the size of power

        damage_counter = Counter(power)
        damage = sorted(damage_counter.keys())
        n = len(damage)
        max_damage = [0] * n
        for i in range(n):
            for j in range(1, 4):
                if i - j >= 0 and damage[i] - damage[i - j] > 2:
                    max_damage[i] = max(max_damage[i], max_damage[i - j])
            max_damage[i] += damage[i] * damage_counter[damage[i]]
            if i - 1 >= 0:
                max_damage[i] = max(max_damage[i], max_damage[i - 1])
        return max(max_damage)
