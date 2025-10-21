from typing import List
from collections import Counter


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums_counter = Counter(nums)
        ranges_counter = Counter()
        endpoints = set(nums)
        for num in nums:
            ranges_counter[num - k] += 1
            endpoints.add(num - k)
            ranges_counter[num + k + 1] -= 1
            endpoints.add(num + k + 1)
        max_frequency = 1
        range_frequency = 0
        for endpoint in sorted(endpoints):
            range_frequency += ranges_counter[endpoint]
            max_frequency = max(
                max_frequency,
                nums_counter[endpoint]
                + min(range_frequency - nums_counter[endpoint], numOperations),
            )
        return max_frequency
