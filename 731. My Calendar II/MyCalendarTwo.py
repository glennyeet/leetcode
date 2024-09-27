from collections import defaultdict


class MyCalendarTwo:

    # def __init__(self):
    #     self.intervals = []
    #     self.overlapping = []

    # def book(self, start: int, end: int) -> bool:
    #     for ol_start, ol_end in self.overlapping:
    #         if start < ol_end and end > ol_start:
    #             return False
    #     for iv_start, iv_end in self.intervals:
    #         if start < iv_end and end > iv_start:
    #             self.overlapping.append((max(start, iv_start), min(end, iv_end)))
    #     self.intervals.append((start, end))
    #     return True

    # Line Sweep algorithm
    def __init__(self):
        self.intervals = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        self.intervals[start] += 1
        self.intervals[end] -= 1
        prefix_sum = 0
        for time in sorted(self.intervals):
            prefix_sum += self.intervals[time]
            if prefix_sum > 2:
                self.intervals[start] -= 1
                self.intervals[end] += 1
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
