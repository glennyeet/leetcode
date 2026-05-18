from typing import List
from collections import defaultdict, deque


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # BFS: O(n) time, O(n) space

        n = len(arr)
        min_jumps = n - 1
        equal_num_indices = defaultdict(list[int])
        for i, num in enumerate(arr):
            equal_num_indices[num].append(i)
        queue = deque([(0, 0)])
        visited = {0}
        while queue:
            i, jumps = queue.popleft()
            if i == n - 1:
                min_jumps = min(min_jumps, jumps)
            next_jumps = jumps + 1
            right = i + 1
            if right < n and right not in visited:
                queue.append((right, next_jumps))
                visited.add(right)
            left = i - 1
            if left >= 0 and left not in visited:
                queue.append((left, next_jumps))
                visited.add(left)
            for j in equal_num_indices[arr[i]]:
                if j != i and j not in visited:
                    queue.append((j, next_jumps))
                    visited.add(j)
            equal_num_indices[arr[i]].clear()
        return min_jumps
