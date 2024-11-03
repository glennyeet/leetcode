from collections import Counter


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        duration_counter = Counter()
        pairs = 0
        for seconds in time:
            seconds %= 60
            duration_counter[seconds] += 1
            paired_seconds = (60 - seconds) % 60
            if seconds == paired_seconds:
                pairs += duration_counter[seconds] - 1
            else:
                pairs += duration_counter[paired_seconds]
        return pairs
