from typing import List


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        # Floyd-Warshall Algorithm: O(n^3) time, O(1) space, where n is the
        # size of original

        total_letters = 26
        min_cost = [[float("inf")] * total_letters for _ in range(total_letters)]
        for x, y, z in zip(original, changed, cost):
            u = ord(x) - ord("a")
            v = ord(y) - ord("a")
            min_cost[u][v] = min(min_cost[u][v], z)
        for k in range(total_letters):
            for i in range(total_letters):
                for j in range(total_letters):
                    min_cost[i][j] = min(
                        min_cost[i][j], min_cost[i][k] + min_cost[k][j]
                    )
        min_source_to_target_cost = 0
        for source_char, target_char in zip(source, target):
            if source_char == target_char:
                continue
            u = ord(source_char) - ord("a")
            v = ord(target_char) - ord("a")
            if min_cost[u][v] == float("inf"):
                return -1
            min_source_to_target_cost += min_cost[u][v]
        return min_source_to_target_cost
