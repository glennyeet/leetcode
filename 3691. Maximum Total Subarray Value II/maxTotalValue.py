from heapq import heappop, heappush
from math import log2
from typing import Any, List


class SparseTable:
    def __init__(self, data: list[int], operation: Any) -> None:
        self.n = len(data)
        self.operation = operation
        self.max_power = int(log2(self.n)) + 1
        self.sparse_table = [[0] * self.max_power for _ in range(self.n)]
        for i in range(self.n):
            self.sparse_table[i][0] = data[i]
        j = 1
        while 1 << j <= self.n:
            i = 0
            while (i + (1 << j) - 1) < self.n:
                self.sparse_table[i][j] = self.operation(
                    self.sparse_table[i][j - 1],
                    self.sparse_table[i + (1 << j - 1)][j - 1],
                )
                i += 1
            j += 1

    def query(self, left: int, right: int) -> int:
        range_length = right - left + 1
        k = int(log2(range_length))
        return self.operation(
            self.sparse_table[left][k], self.sparse_table[right - (1 << k) + 1][k]
        )


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # Sparse Tree + Priority Queue: O(n * log(n) + k * log(n)) time,
        # O(n * log(n)) space

        n = len(nums)
        min_sparse_table = SparseTable(nums, min)
        max_sparse_table = SparseTable(nums, max)
        left = 0
        right = n - 1
        total_value = 0
        priority_queue = []
        subarrays = set()
        heappush(
            priority_queue,
            (
                -(
                    max_sparse_table.query(left, right)
                    - min_sparse_table.query(left, right)
                ),
                left,
                right,
            ),
        )
        subarrays.add((left, right))
        for _ in range(k):
            value, left, right = heappop(priority_queue)
            total_value += -value
            new_left = left + 1
            if new_left <= right and (new_left, right) not in subarrays:
                subarrays.add((new_left, right))
                heappush(
                    priority_queue,
                    (
                        -(
                            max_sparse_table.query(new_left, right)
                            - min_sparse_table.query(new_left, right)
                        ),
                        new_left,
                        right,
                    ),
                )
            new_right = right - 1
            if new_right >= left and (left, new_right) not in subarrays:
                subarrays.add((left, new_right))
                heappush(
                    priority_queue,
                    (
                        -(
                            max_sparse_table.query(left, new_right)
                            - min_sparse_table.query(left, new_right)
                        ),
                        left,
                        new_right,
                    ),
                )
        return total_value
