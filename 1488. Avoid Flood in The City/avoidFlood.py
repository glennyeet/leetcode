from typing import List
from sortedcontainers import SortedList


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # Greedy: O(n * log(n)) time, O(n) space

        n = len(rains)
        full_lakes = {}
        dry_operations = SortedList()
        ans = [-1] * n
        for i, lake in enumerate(rains):
            if lake == 0:
                dry_operations.add(i)
            elif lake in full_lakes:
                j = dry_operations.bisect_left(full_lakes[lake])
                if j == len(dry_operations):
                    return []
                dry_operation = dry_operations[j]
                ans[dry_operation] = lake
                dry_operations.remove(dry_operation)
            full_lakes[lake] = i
        for dry_operation in dry_operations:
            ans[dry_operation] = 1
        return ans
