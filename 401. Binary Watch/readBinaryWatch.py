from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # Bit Manipulation: O(1) time, O(1) space

        valid_times = []
        for hour in range(0, 12):
            for minute in range(0, 60):
                if hour.bit_count() + minute.bit_count() == turnedOn:
                    time = str(hour) + ":"
                    if minute < 10:
                        time += "0"
                    time += str(minute)
                    valid_times.append(time)
        return valid_times
