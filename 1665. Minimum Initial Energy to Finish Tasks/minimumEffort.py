from typing import List


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Greedy: O(n * log(n)) time, O(n) space, where n is
        # the size of tasks

        sorted_tasks = sorted(tasks, key=lambda x: x[1] - x[0])
        min_effort = 0
        for task in sorted_tasks:
            min_effort = max(min_effort + task[0], task[1])
        return min_effort
