from collections import defaultdict


class MyCalendarThree:

    def __init__(self):
        self.intervals = defaultdict(int)
        self.k = 1

    def book(self, startTime: int, endTime: int) -> int:
        self.intervals[startTime] += 1
        self.intervals[endTime] -= 1
        prefix_sum = 0
        for time in sorted(self.intervals):
            prefix_sum += self.intervals[time]
            self.k = max(self.k, prefix_sum)
        return self.k


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
