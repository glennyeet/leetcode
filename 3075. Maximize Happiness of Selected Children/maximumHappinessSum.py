from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # Greedy: O(n * log(n)) time, O(n) space, where n is the size
        # of happiness

        selected_children = sorted(happiness, reverse=True)[:k]
        max_sum = 0
        penalty = 0
        for happiness_value in selected_children:
            max_sum += max(0, happiness_value - penalty)
            penalty += 1
        return max_sum
