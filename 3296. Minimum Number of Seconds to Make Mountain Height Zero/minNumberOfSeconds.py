from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # Priority Queue: O(h * log(n)) time, O(n) space, where h is mountainHeight
        # and n is the size of workerTimes

        priority_queue = []
        for time in workerTimes:
            priority_queue.append((time, time, 1))
        heapify(priority_queue)
        while mountainHeight > 1:
            seconds_elapsed, worker_time, height_decreased = heappop(priority_queue)
            height_decreased += 1
            heappush(
                priority_queue,
                (
                    seconds_elapsed + worker_time * height_decreased,
                    worker_time,
                    height_decreased,
                ),
            )
            mountainHeight -= 1
        return heappop(priority_queue)[0]
