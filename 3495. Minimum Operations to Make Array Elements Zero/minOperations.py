from typing import List


class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        # Math: O(qlog(r)) time, O(1) space, where q is the size of
        # queries and r is the end range of each query

        def count_min_divisions(r: int) -> int:
            min_divisions = 0
            k = 1
            num = 1
            while r >= num * 4:
                min_divisions += (num * 4 - num) * k
                k += 1
                num *= 4
            else:
                min_divisions += (r - num + 1) * k
            return min_divisions

        total_operations = 0
        for l, r in queries:
            total_operations += (
                count_min_divisions(r) - count_min_divisions(l - 1) + 1
            ) // 2
        return total_operations
