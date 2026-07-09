from typing import List


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        # Union-Find: O((α(n) * (n + q)) time, O(n + q) space, where q is the
        # size of queries

        parent = [x for x in range(n)]

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> None:
            px = find(x)
            py = find(y)
            if px != py:
                parent[py] = px

        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                union(i, i - 1)
        answer = []
        for u, v in queries:
            answer.append(find(u) == find(v))
        return answer
