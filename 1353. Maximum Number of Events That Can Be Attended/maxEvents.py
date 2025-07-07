from typing import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Greedy: O(nlog(n)) time, O(n) space, where
        # n is the size of events

        events_dict = defaultdict(list)
        for start, end in events:
            events_dict[start].append(end)
        pending_events = []
        cur_day = 1
        max_events = 0
        for start in sorted(events_dict):
            while pending_events and cur_day < start:
                end = heappop(pending_events)
                if cur_day <= end:
                    cur_day += 1
                    max_events += 1
            cur_day = start
            for end in events_dict[start]:
                heappush(pending_events, end)
        while pending_events:
            end = heappop(pending_events)
            if cur_day <= end:
                cur_day += 1
                max_events += 1
        return max_events
