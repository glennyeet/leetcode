from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        # Array: O(n) time, O(1) space

        n = len(words)
        min_dist = float("inf")
        for i in range(n):
            if words[i] == target:
                min_dist = min(
                    min_dist,
                    abs(i - startIndex),
                    abs(startIndex + n - i),
                    abs(i + n - startIndex),
                )
        if min_dist == float("inf"):
            return -1
        return min_dist
