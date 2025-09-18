from typing import List
from heapq import heapify, heappush, heappop


class TaskManager:
    # Hash Table + Priority Queue

    def __init__(self, tasks: List[List[int]]):
        # O(n) time, O(n) space, where n is the size of tasks

        self.lookup = {}
        self.priority_queue = []
        for user_id, task_id, priority in tasks:
            version = 1
            self.lookup[task_id] = (user_id, version)
            self.priority_queue.append((-priority, -task_id, user_id, version))
        heapify(self.priority_queue)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        # O(1) time, O(1) space

        if taskId in self.lookup:
            _, version = self.lookup[taskId]
        else:
            version = 0
        self.lookup[taskId] = (userId, version + 1)
        heappush(self.priority_queue, (-priority, -taskId, userId, version + 1))

    def edit(self, taskId: int, newPriority: int) -> None:
        # O(1) time, O(1) space

        user_id, version = self.lookup[taskId]
        self.lookup[taskId] = (user_id, version + 1)
        heappush(self.priority_queue, (-newPriority, -taskId, user_id, version + 1))

    def rmv(self, taskId: int) -> None:
        # O(1) time, O(1) space

        user_id, version = self.lookup[taskId]
        self.lookup[taskId] = (user_id, version + 1)

    def execTop(self) -> int:
        # O(nlog(n)) time, O(1) space

        if not self.priority_queue:
            return -1
        while self.priority_queue:
            _, task_id, user_id, entry_version = self.priority_queue[0]
            task_id = -task_id
            _, cur_version = self.lookup[task_id]
            if entry_version < cur_version:
                heappop(self.priority_queue)
            else:
                break
        if self.priority_queue:
            heappop(self.priority_queue)
            return user_id
        else:
            return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
