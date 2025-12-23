from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Greedy: O(n * log(n)) time, O(n) space, where n
        # is the size of events

        sorted_events = []
        for start, end, value in events:
            sorted_events.append((start, -1, value))
            sorted_events.append((end, 1, value))
        sorted_events.sort()
        max_sum = float("-inf")
        max_event = float("-inf")
        for _, type, value in sorted_events:
            if type == -1:
                max_sum = max(max_sum, max_event + value)
            else:
                max_event = max(max_event, value)
                max_sum = max(max_sum, value)
        return max_sum
