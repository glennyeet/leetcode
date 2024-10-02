from collections import Counter


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        counter = Counter()
        pairs = 0
        for time in hours:
            time %= 24
            second_time = (24 - time) % 24
            counter[time] += 1
            if not counter[second_time]:
                continue
            if time == second_time:
                pairs += counter[time] - 1
            else:
                pairs += counter[second_time]
        return pairs
