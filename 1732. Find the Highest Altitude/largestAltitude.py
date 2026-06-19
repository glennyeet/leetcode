from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # Math: O(n) time, O(1) space, where n is the
        # size of gain

        max_altitude = 0
        cur_altitude = 0
        for delta in gain:
            cur_altitude += delta
            max_altitude = max(max_altitude, cur_altitude)
        return max_altitude
