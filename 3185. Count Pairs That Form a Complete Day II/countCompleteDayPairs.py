from collections import Counter


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        pairs = 0
        hours_counter = Counter()
        for hour in hours:
            hour %= 24
            hours_counter[hour] += 1
            paired_hour = (24 - hour) % 24
            if paired_hour == hour:
                pairs += hours_counter[paired_hour] - 1
            else:
                pairs += hours_counter[paired_hour]
        return pairs
