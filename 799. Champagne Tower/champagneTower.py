class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Bottom-up DP: O(r^2) time, O(r) space, where r is query_row

        capacity = [poured]
        for row in range(1, query_row + 1):
            new_capacity = [0.0] * (row + 1)
            for glass in range(len(capacity)):
                overflow = max(0, capacity[glass] - 1)
                new_capacity[glass] += overflow / 2
                new_capacity[glass + 1] += overflow / 2
            capacity = new_capacity
        return min(1.0, capacity[query_glass])
