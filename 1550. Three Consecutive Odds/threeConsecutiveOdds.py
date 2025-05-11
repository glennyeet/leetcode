from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # Brute Force: O(n) time, O(1) space, where n is
        # the size of arr

        streak = 0
        for num in arr:
            if num % 2:
                streak += 1
            else:
                streak = 0
            if streak == 3:
                return True
        return False
