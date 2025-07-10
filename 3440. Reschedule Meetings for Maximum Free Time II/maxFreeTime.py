from typing import List


class Solution:
    def maxFreeTime(
        self, eventTime: int, startTime: List[int], endTime: List[int]
    ) -> int:
        # Greedy: O(n) time, O(n) space

        start_times = [-1] + startTime + [eventTime]
        end_times = [0] + endTime + [10**9 + 1]
        n = len(start_times)
        max_left_free_time = [0]
        for i in range(1, n):
            max_left_free_time.append(
                max(max_left_free_time[-1], start_times[i] - end_times[i - 1])
            )
        max_right_free_time = [0]
        for i in reversed(range(n - 1)):
            max_right_free_time.append(
                max(max_right_free_time[-1], start_times[i + 1] - end_times[i])
            )
        max_right_free_time.reverse()
        max_free_time = 0
        for i in range(1, n - 1):
            total_time = start_times[i + 1] - end_times[i - 1]
            meeting_time = end_times[i] - start_times[i]
            if (
                max_left_free_time[i - 1] >= meeting_time
                or max_right_free_time[i + 1] >= meeting_time
            ):
                max_free_time = max(max_free_time, total_time)
            max_free_time = max(
                max_free_time,
                total_time - meeting_time,
            )
        return max_free_time
