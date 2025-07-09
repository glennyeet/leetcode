from typing import List


class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:
        # Greedy + Sliding Window: O(n) time, O(1) space

        n = len(startTime)
        meeting_time = 0
        for i in range(k):
            meeting_time += endTime[i] - startTime[i]
        if k == n:
            return eventTime - meeting_time
        max_free_time = startTime[k] - meeting_time
        l = 0
        for r in range(k, n):
            meeting_time += (endTime[r] - startTime[r]) - (endTime[l] - startTime[l])
            if r == n - 1:
                max_free_time = max(
                    max_free_time, eventTime - endTime[l] - meeting_time
                )
            else:
                max_free_time = max(
                    max_free_time, startTime[r + 1] - endTime[l] - meeting_time
                )
            l += 1
        return max_free_time
