from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        # Binary Search: O(n * log(n) + m * log(n)) time,
        # O(n) space, where m is the size of spells

        n = len(potions)
        sorted_potions = sorted(potions)
        pairs = []
        for spell in spells:
            min_potion_index = n
            left = 0
            right = n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if spell * sorted_potions[mid] < success:
                    left = mid + 1
                else:
                    min_potion_index = mid
                    right = mid - 1
            pairs.append(n - min_potion_index)
        return pairs
