from typing import List
from collections import defaultdict


class Solution:
    def mostProfitablePath(
        self, edges: List[List[int]], bob: int, amount: List[int]
    ) -> int:
        # DFS: O(n) time, O(n) space

        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        bob_timestamps = {}

        def get_bob_timestamps(cur_node: int, parent_node: int, time: int) -> bool:
            if cur_node == 0:
                bob_timestamps[cur_node] = time
                return True
            for child_node in adj_list[cur_node]:
                if child_node != parent_node and get_bob_timestamps(
                    child_node, cur_node, time + 1
                ):
                    bob_timestamps[cur_node] = time
                    return True
            return False

        get_bob_timestamps(bob, None, 0)

        def get_alice_max_income(
            cur_node: int, parent_node: int, time: int, income: int
        ) -> int:
            if cur_node not in bob_timestamps or time < bob_timestamps[cur_node]:
                new_income = income + amount[cur_node]
            elif time > bob_timestamps[cur_node]:
                new_income = income
            else:
                new_income = income + amount[cur_node] // 2
            child_nodes = adj_list[cur_node]
            if len(child_nodes) == 1 and child_nodes[0] == parent_node:
                return new_income
            max_income = float("-inf")
            for child_node in child_nodes:
                if child_node != parent_node:
                    max_income = max(
                        max_income,
                        get_alice_max_income(
                            child_node, cur_node, time + 1, new_income
                        ),
                    )
            return max_income

        return get_alice_max_income(0, None, 0, 0)
