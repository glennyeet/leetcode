from heapq import heapify, heappop, heappush


class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # Priority Queue: O(m * log(n)) time, O(m + n) space

        n = len(servers)
        m = len(tasks)
        ans = [None] * m
        free_servers = [(servers[i], i) for i in range(n)]
        heapify(free_servers)
        busy_servers = []
        t = 0
        for task_idx in range(m):
            t = max(t, task_idx)
            if not free_servers:
                t = max(t, busy_servers[0][0])
            while busy_servers and busy_servers[0][0] <= t:
                _, weight, server_idx = heappop(busy_servers)
                heappush(free_servers, (weight, server_idx))
            weight, server_idx = heappop(free_servers)
            ans[task_idx] = server_idx
            heappush(busy_servers, (t + tasks[task_idx], weight, server_idx))
        return ans
