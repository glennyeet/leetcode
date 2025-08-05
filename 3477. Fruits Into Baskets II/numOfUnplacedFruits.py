from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # Brute Force: O(n^2) time, O(n) space

        n = len(fruits)
        filled_baskets = set()
        unplaced_fruits = 0
        for i in range(n):
            for j in range(n):
                if fruits[i] <= baskets[j] and j not in filled_baskets:
                    filled_baskets.add(j)
                    break
            else:
                unplaced_fruits += 1
        return unplaced_fruits
