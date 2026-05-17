from typing import List
from collections import deque


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # BFS: O(n) time, O(n) space

        n = len(arr)
        queue = deque([start])
        visited = set()
        while queue:
            i = queue.popleft()
            visited.add(i)
            if arr[i] == 0:
                return True
            left = i - arr[i]
            right = i + arr[i]
            if left >= 0 and left not in visited:
                queue.append(left)
            if right < n and right not in visited:
                queue.append(right)
        return False
