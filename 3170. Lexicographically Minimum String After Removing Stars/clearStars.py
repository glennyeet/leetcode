from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def clearStars(self, s: str) -> str:
        # Greedy + Hash Table + Priority Queue: O(n) time, O(n) space,
        # where n is the size of s

        char_indices = defaultdict(list)
        priority_queue = []
        deleted_char_indices = set()
        for i, char in enumerate(s):
            if char == "*":
                deleted_char = heappop(priority_queue)
                deleted_char_indices.add(char_indices[deleted_char].pop())
                if len(char_indices[deleted_char]):
                    heappush(priority_queue, deleted_char)
            else:
                char_indices[char].append(i)
                if len(char_indices[char]) == 1:
                    heappush(priority_queue, char)
        smallest_string = []
        for i, char in enumerate(s):
            if char != "*" and i not in deleted_char_indices:
                smallest_string.append(char)
        return "".join(smallest_string)
