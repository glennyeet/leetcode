from collections import defaultdict
from typing import List


class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        # DFS: O(n) time, O(n) space

        adj_list = defaultdict(list)
        for a, b in invocations:
            adj_list[a].append(b)
        suspicious_methods = set()
        visited = set()

        def find_suspicious_methods(a: int) -> None:
            suspicious_methods.add(a)
            visited.add(a)
            for b in adj_list[a]:
                if b not in visited:
                    find_suspicious_methods(b)

        find_suspicious_methods(k)
        for a, b in invocations:
            if a not in suspicious_methods and b in suspicious_methods:
                return list(range(n))
        clean_methods = []
        for a in range(n):
            if a not in suspicious_methods:
                clean_methods.append(a)
        return clean_methods
