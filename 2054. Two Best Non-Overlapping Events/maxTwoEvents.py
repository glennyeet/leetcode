from heapq import heappush, heappop


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        sorted_events = events.copy()
        sorted_events.sort()
        prev_max = 0
        max_sum = 0
        prev_events = []
        for start_time, end_time, value in sorted_events:
            while prev_events and prev_events[0][0] < start_time:
                _, prev_value = heappop(prev_events)
                prev_max = max(prev_max, prev_value)
            max_sum = max(max_sum, prev_max + value)
            heappush(prev_events, (end_time, value))
        return max_sum
