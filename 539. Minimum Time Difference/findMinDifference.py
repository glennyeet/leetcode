class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def compare_times(time1: str, time2: str) -> int:
            if time1 == time2:
                return 0
            if (
                time1[:2] > time2[:2]
                or time1[:2] == time2[:2]
                and time1[3:] > time2[3:]
            ):
                return 1
            return -1

        def merge_sort(times: list[str]):
            if len(times) > 1:
                mid = len(times) // 2
                left = times[:mid]
                right = times[mid:]
                merge_sort(left)
                merge_sort(right)
                i = j = k = 0
                while i < len(left) and j < len(right):
                    if compare_times(left[i], right[j]) == -1:
                        times[k] = left[i]
                        i += 1
                    else:
                        times[k] = right[j]
                        j += 1
                    k += 1
                while i < len(left):
                    times[k] = left[i]
                    i += 1
                    k += 1
                while j < len(right):
                    times[k] = right[j]
                    j += 1
                    k += 1

        def find_minutes_diff(time1: str, time2: str) -> int:
            # time1 <= time2
            if time1 == time2:
                return 0
            hours1 = int(time1[:2])
            hours2 = int(time2[:2])
            minutes1 = int(time1[3:])
            minutes2 = int(time2[3:])
            if minutes1 > minutes2:
                hours = hours2 - hours1 - 1
                minutes = 60 - minutes1 + minutes2
            else:
                hours = hours2 - hours1
                minutes = minutes2 - minutes1
            return hours * 60 + minutes

        # timePoints.sort()
        merge_sort(timePoints)
        min_diff = (
            find_minutes_diff(timePoints[-1], "23:59")
            + find_minutes_diff("00:00", timePoints[0])
            + 1
        )
        for time1, time2 in zip(timePoints, timePoints[1:]):
            min_diff = min(min_diff, find_minutes_diff(time1, time2))
        return min_diff
