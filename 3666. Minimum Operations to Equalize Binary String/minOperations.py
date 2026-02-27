from sortedcontainers import SortedList
from collections import deque


class Solution:
    def minOperations(self, s: str, k: int) -> int:
        # BFS + Binary Search + Queue: O(n * log(n)) time, O(n) space

        n = len(s)
        even_nums = SortedList()
        odd_nums = SortedList()
        for i in range(n + 1):
            if i % 2:
                odd_nums.add(i)
            else:
                even_nums.add(i)
        ones = s.count("1")
        min_operations = [float("inf")] * (n + 1)
        min_operations[ones] = 0
        if ones == n:
            return min_operations[ones]
        if ones % 2:
            odd_nums.remove(ones)
        else:
            even_nums.remove(ones)
        queue = deque()
        queue.append(ones)
        while queue:
            ones = queue.popleft()
            if ones >= k:
                lower_bound = ones - k
            else:
                delta = ones - (k - ones)
                lower_bound = ones - delta
            if (ones + k) % 2:
                next_frontier = odd_nums
            else:
                next_frontier = even_nums
            zeroes = n - ones
            if zeroes >= k:
                upper_bound = ones + k
            else:
                delta = zeroes - (k - zeroes)
                upper_bound = ones + delta
            while True:
                i = next_frontier.bisect_left(lower_bound)
                if i >= len(next_frontier) or next_frontier[i] > upper_bound:
                    break
                new_ones = next_frontier[i]
                next_frontier.remove(new_ones)
                queue.append(new_ones)
                min_operations[new_ones] = min_operations[ones] + 1
                if new_ones == n:
                    return min_operations[new_ones]
        return -1
