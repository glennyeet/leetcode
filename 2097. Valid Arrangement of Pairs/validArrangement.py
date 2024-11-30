from collections import deque, Counter, defaultdict


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # Hierholzer's algorithm

        out_degree = Counter()
        in_degree = Counter()
        adj_list = defaultdict(list)
        for u, v in pairs:
            out_degree[u] += 1
            in_degree[v] += 1
            adj_list[u].append(v)
        start_node = None
        for u in out_degree:
            if out_degree[u] - in_degree[u] == 1:
                start_node = u
                break
            if out_degree[u] > 0:
                start_node = u
        path = deque()

        def dfs(u: int):
            while out_degree[u] != 0:
                v = adj_list[u].pop()
                out_degree[u] -= 1
                dfs(v)
            path.appendleft(u)

        dfs(start_node)
        arrangement = []
        for i in range(len(path) - 1):
            arrangement.append([path[i], path[i + 1]])
        return arrangement
