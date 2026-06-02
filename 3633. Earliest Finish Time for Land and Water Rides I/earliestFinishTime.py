from typing import List


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        # Brute Force: O(n * m) time, O(1) space, where n is the size of
        # landStartTime and m is the size of waterStartTime

        min_finish_time = float("inf")
        for l_start, l_duration in zip(landStartTime, landDuration):
            min_l_end = l_start + l_duration
            for w_start, w_duration in zip(waterStartTime, waterDuration):
                min_w_end = w_start + w_duration
                if w_start < min_l_end:
                    min_finish_time = min(min_finish_time, min_l_end + w_duration)
                else:
                    min_finish_time = min(min_finish_time, min_w_end)
                if l_start < min_w_end:
                    min_finish_time = min(min_finish_time, min_w_end + l_duration)
                else:
                    min_finish_time = min(min_finish_time, min_l_end)
        return min_finish_time
