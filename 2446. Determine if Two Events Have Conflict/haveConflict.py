class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def convertToMinutes(time: str) -> int:
            return int(time[:2]) * 60 + int(time[3:])

        event1_start = convertToMinutes(event1[0])
        event1_end = convertToMinutes(event1[1])
        event2_start = convertToMinutes(event2[0])
        event2_end = convertToMinutes(event2[1])
        if event1_start <= event2_end and event1_end >= event2_start:
            return True
        return False
