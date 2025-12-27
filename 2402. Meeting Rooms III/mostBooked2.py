from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Priority Queue: O(n * log(n)) time, O(n) space

        ongoing_meetings = []
        available_rooms = []
        for i in range(n):
            available_rooms.append(i)
        heapify(available_rooms)
        meetings_count = [0] * n
        for start, end in sorted(meetings):
            while ongoing_meetings and ongoing_meetings[0][0] <= start:
                _, free_room = heappop(ongoing_meetings)
                heappush(available_rooms, free_room)
            if len(ongoing_meetings) == n:
                available_time, free_room = heappop(ongoing_meetings)
                heappush(ongoing_meetings, (available_time + (end - start), free_room))
            else:
                free_room = heappop(available_rooms)
                heappush(ongoing_meetings, (end, free_room))
            meetings_count[free_room] += 1
        return meetings_count.index(max(meetings_count))
