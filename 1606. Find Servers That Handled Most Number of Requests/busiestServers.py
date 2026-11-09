from heapq import heappop, heappush
from sortedcontainers import SortedList


class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # Sorted List + Priority Queue: O((k + n) * log(k)) time, O(k) space, where n
        # is the size of arrival

        free_servers = SortedList(i for i in range(k))
        busy_servers = []
        requests_handled = [0] * k
        for i, (arrival_time, request_load) in enumerate(zip(arrival, load)):
            while busy_servers and busy_servers[0][0] <= arrival_time:
                _, server = heappop(busy_servers)
                free_servers.add(server)
            if not free_servers:
                continue
            selected_server = free_servers.bisect_left(i % k)
            if selected_server >= len(free_servers):
                server = free_servers[0]
            else:
                server = free_servers[selected_server]
            requests_handled[server] += 1
            free_servers.remove(server)
            heappush(busy_servers, (arrival_time + request_load, server))
        max_requests_handled = max(requests_handled)
        busiest_servers = []
        for i, requests in enumerate(requests_handled):
            if requests == max_requests_handled:
                busiest_servers.append(i)
        return busiest_servers
