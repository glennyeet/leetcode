from typing import List

# from sortedcontainers import SortedList
from collections import deque


class Solution:
    def maxTaskAssign(
        self, tasks: List[int], workers: List[int], pills: int, strength: int
    ) -> int:
        # Binary Search + Greedy: O(tlog(t) + wlog(w) + log(min(t, w)) * (tlog(min(t, w)) + wlog(min(t, w)))) time,
        # O(t + w) space

        # t = len(tasks)
        # w = len(workers)
        # sorted_tasks = sorted(tasks, reverse=True)
        # sorted_workers = sorted(workers, reverse=True)

        # def can_assign_all_tasks(tasks_start_index: int) -> bool:
        #     cur_workers = SortedList(sorted_workers)
        #     cur_pills = pills
        #     for i in range(tasks_start_index, t):
        #         if cur_workers[-1] >= sorted_tasks[i]:
        #             cur_workers.pop()
        #         else:
        #             if cur_pills == 0:
        #                 return False
        #             cur_pills -= 1
        #             worker_index = cur_workers.bisect_left(sorted_tasks[i] - strength)
        #             if worker_index >= len(cur_workers):
        #                 return False
        #             cur_workers.remove(cur_workers[worker_index])
        #     return True

        # low = 0
        # high = min(t, w)
        # max_tasks = 0
        # while low <= high:
        #     mid = (low + high) // 2
        #     if can_assign_all_tasks(t - mid):
        #         max_tasks = mid
        #         low = mid + 1
        #     else:
        #         high = mid - 1
        # return max_tasks

        # Binary Search + Greedy: O(tlog(t) + wlog(w) + (w + t)log(min(t, w))) time,
        # O(t + w) time

        t = len(tasks)
        w = len(workers)
        sorted_tasks = sorted(tasks)
        sorted_workers = sorted(workers)

        def can_assign_all_tasks(max_tasks: int) -> bool:
            available_tasks = deque()
            j = 0
            cur_pills = pills
            for i in range(w - max_tasks, w):
                while j < max_tasks and sorted_tasks[j] <= sorted_workers[i] + strength:
                    available_tasks.append(sorted_tasks[j])
                    j += 1
                if len(available_tasks) == 0:
                    return False
                elif available_tasks[0] <= sorted_workers[i]:
                    available_tasks.popleft()
                else:
                    if cur_pills == 0:
                        return False
                    cur_pills -= 1
                    available_tasks.pop()
            return True

        low = 0
        high = min(t, w)
        max_tasks = 0
        while low <= high:
            mid = (low + high) // 2
            if can_assign_all_tasks(mid):
                max_tasks = mid
                low = mid + 1
            else:
                high = mid - 1
        return max_tasks
