from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Greedy + Priority Queue: O(nlog(n)) time, O(n) space

        n = len(classes)
        pass_ratios = []
        for passes, total in classes:
            pass_ratios.append(
                (-((passes + 1) / (total + 1) - passes / total), passes, total)
            )
        heapify(pass_ratios)
        extra_students_left = extraStudents
        while extra_students_left > 0:
            extra_students_left -= 1
            _, passes, total = heappop(pass_ratios)
            new_passes = passes + 1
            new_total = total + 1
            heappush(
                pass_ratios,
                (
                    -((new_passes + 1) / (new_total + 1) - new_passes / new_total),
                    new_passes,
                    new_total,
                ),
            )
        pass_ratios_sum = 0
        for _, passes, total in pass_ratios:
            pass_ratios_sum += passes / total
        return pass_ratios_sum / n
