class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # def compare_times(time1: str, time2: str) -> int:
        #     if time1[:2] > time2[:2]:
        #         return 1
        #     if time1[3:] > time2[3:]:
        #         return 1
        #     if time1 == time2:
        #         return 0
        #     return -1

        def find_minutes_diff(time1: str, time2: str) -> int:
            # time1 <= time2
            if time1 == time2:
                return 0
            hours1 = int(time1[:2])
            hours2 = int(time2[:2])
            minutes1 = int(time1[3:])
            minutes2 = int(time2[3:])
            hours = hours2 - hours1
            if minutes1 > minutes2:
                hours -= 1
            if minutes1 > minutes2:
                minutes = 60 - minutes1 + minutes2
            else:
                minutes = minutes2 - minutes1
            return hours * 60 + minutes

        timePoints.sort()
        min_diff = (
            find_minutes_diff(timePoints[-1], "23:59")
            + find_minutes_diff("00:00", timePoints[0])
            + 1
        )
        for time1, time2 in zip(timePoints, timePoints[1:]):
            min_diff = min(min_diff, find_minutes_diff(time1, time2))
        return min_diff
