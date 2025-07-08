from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Bottom-up DP: O(elog(e) + e * k) time, O(e + k) space,
        # where e is the size of events

        events_dict = defaultdict(list)
        events_dict[10**9 + 1]
        for start, end, value in events:
            events_dict[start].append((end, value))
        max_sums = [0] * (k + 1)
        pending_events = []
        for start in sorted(events_dict):
            while pending_events and pending_events[0][0] <= start:
                _, new_max_sums = heappop(pending_events)
                for i in range(1, k + 1):
                    max_sums[i] = max(max_sums[i], new_max_sums[i])
            for end, value in events_dict[start]:
                new_max_sums = [0] * (k + 1)
                for i in range(k):
                    new_max_sums[i + 1] = max_sums[i] + value
                heappush(pending_events, (end + 1, new_max_sums))
        return max(max_sums)
