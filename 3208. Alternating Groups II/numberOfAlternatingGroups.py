from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # Sliding window: O(n) time, O(1) space

        n = len(colors)
        i = 0
        j = 0
        alternating_groups = 0
        while i < n:
            while j - i + 1 < k and colors[j % n] != colors[(j + 1) % n]:
                j += 1
            if j - i + 1 == k:
                alternating_groups += 1
                i += 1
            elif colors[j % n] == colors[(j + 1) % n]:
                j += 1
                i = j
        return alternating_groups
