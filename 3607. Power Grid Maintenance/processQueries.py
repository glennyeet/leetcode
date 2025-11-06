from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def processQueries(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        # Hash Table + Priority Queue + DFS: O(e + q + c * log(c)) time,
        # O(e + c + q) space, where e is the size of connections and q is
        # the size of queries

        adj_list = defaultdict(list)
        for u, v in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)
        online_stations = set()
        station_group = {}
        group_pqs = defaultdict(list)

        def dfs(station: int, group: int) -> None:
            if station in online_stations:
                return
            online_stations.add(station)
            station_group[station] = group
            heappush(group_pqs[group], station)
            for neighbour in adj_list[station]:
                dfs(neighbour, group)

        for station in range(1, c + 1):
            dfs(station, station)
        maintenance_checks = []
        for type, station in queries:
            if type == 1:
                if station in online_stations:
                    maintenance_checks.append(station)
                else:
                    group = station_group[station]
                    group_pq = group_pqs[group]
                    while group_pq and group_pq[0] not in online_stations:
                        heappop(group_pq)
                    if group_pq:
                        maintenance_checks.append(group_pq[0])
                    else:
                        maintenance_checks.append(-1)
            else:
                online_stations.discard(station)
        return maintenance_checks
