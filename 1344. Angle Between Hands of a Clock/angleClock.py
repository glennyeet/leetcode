class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Math: O(1) time, O(1) space

        minute_angle = minutes / 60 * 360
        hour_angle = hour % 12 * 30 + minutes / 60 * 30
        angle_diff = abs(minute_angle - hour_angle)
        return min(angle_diff, 360 - angle_diff)
