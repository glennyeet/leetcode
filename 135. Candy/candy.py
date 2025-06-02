from typing import List
from collections import deque


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Topological Sort: O(n) time, O(n) space

        n = len(ratings)
        in_degree = [0] * n
        queue = deque()
        for i in range(n):
            if i > 0 and ratings[i] > ratings[i - 1]:
                in_degree[i] += 1
            if i < n - 1 and ratings[i] > ratings[i + 1]:
                in_degree[i] += 1
            if not in_degree[i]:
                queue.append(i)
        candies = [float("inf")] * n
        while queue:
            cur_child = queue.popleft()
            cur_candies = 1
            if cur_child > 0 and ratings[cur_child] > ratings[cur_child - 1]:
                cur_candies = max(cur_candies, candies[cur_child - 1] + 1)
            if cur_child < n - 1 and ratings[cur_child] > ratings[cur_child + 1]:
                cur_candies = max(cur_candies, candies[cur_child + 1] + 1)
            candies[cur_child] = cur_candies
            if cur_child > 0 and ratings[cur_child] < ratings[cur_child - 1]:
                in_degree[cur_child - 1] -= 1
                if not in_degree[cur_child - 1]:
                    queue.append(cur_child - 1)
            if cur_child < n - 1 and ratings[cur_child] < ratings[cur_child + 1]:
                in_degree[cur_child + 1] -= 1
                if not in_degree[cur_child + 1]:
                    queue.append(cur_child + 1)
        return sum(candies)
