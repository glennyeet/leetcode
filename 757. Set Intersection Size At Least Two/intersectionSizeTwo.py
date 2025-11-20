from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Greedy: O(n * log(n)) time, O(n) space, where n is the size
        # of intervals

        sorted_intervals = sorted(intervals, key=lambda i: (i[1], -i[0]))
        min_containing_set_size = 0
        i_1 = -1
        i_2 = -1
        for start, end in sorted_intervals:
            if i_2 < start:
                min_containing_set_size += 2
                i_1 = end - 1
                i_2 = end
            elif i_1 < start:
                min_containing_set_size += 1
                i_1 = i_2
                i_2 = end
        return min_containing_set_size
