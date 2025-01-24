class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # DFS: O(n + m) time, O(n) space, where m is the number of
        # edges in graph

        n = len(graph)
        visited = [False] * n
        safe = [False] * n

        def is_safe(node: int) -> bool:
            if visited[node]:
                return safe[node]
            visited[node] = True
            for neighbour in graph[node]:
                if not is_safe(neighbour):
                    return False
            safe[node] = True
            return True

        safe_nodes = []
        for i in range(n):
            if is_safe(i):
                safe_nodes.append(i)
        return safe_nodes
