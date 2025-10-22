from typing import List
from collections import Counter


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # Line Sweep: O(n * log(n)) time, O(n) space, where n is the size of
        # nums

        nums_counter = Counter()
        ranges_counter = Counter()
        points = set()
        for num in nums:
            nums_counter[num] += 1
            points.add(num)
            ranges_counter[num - k] += 1
            points.add(num - k)
            ranges_counter[num + k + 1] -= 1
            points.add(num + k + 1)
        max_frequency = 1
        range_overlaps = 0
        for point in sorted(points):
            range_overlaps += ranges_counter[point]
            max_frequency = max(
                max_frequency,
                nums_counter[point]
                + min(numOperations, range_overlaps - nums_counter[point]),
            )
        return max_frequency
