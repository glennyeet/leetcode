from typing import List


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        # Greedy: O(n + m) time, O(1) space, where n is the size of
        # landStartTime and m is the size of waterStartTime

        min_land_end = float("inf")
        for land_start, land_time in zip(landStartTime, landDuration):
            min_land_end = min(min_land_end, land_start + land_time)
        min_water_end = float("inf")
        for water_start, water_time in zip(waterStartTime, waterDuration):
            min_water_end = min(min_water_end, water_start + water_time)
        min_finish_time = float("inf")
        for land_start, land_time in zip(landStartTime, landDuration):
            min_finish_time = min(
                min_finish_time, max(min_water_end, land_start) + land_time
            )
        for water_start, water_time in zip(waterStartTime, waterDuration):
            min_finish_time = min(
                min_finish_time, max(min_land_end, water_start) + water_time
            )
        return min_finish_time
