from typing import List
from collections import defaultdict


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # Line sweep: (O(nlog(n))) time, O(n) space, where n is days

        meetings_count = defaultdict(int)
        for day, end in meetings:
            meetings_count[day] += 1
            meetings_count[end + 1] -= 1
        active_meetings = 0
        prev_day = 1
        no_meeting_days = 0
        for day in sorted(meetings_count.keys()):
            if not active_meetings:
                no_meeting_days += day - prev_day
            active_meetings += meetings_count[day]
            prev_day = day
        no_meeting_days += days - prev_day + 1
        return no_meeting_days
