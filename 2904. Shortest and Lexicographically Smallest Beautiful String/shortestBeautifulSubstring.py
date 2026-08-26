from collections import deque


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # Sliding Window: O(n) time, O(n) space

        n = len(s)
        min_substring = "2" * (n + 1)
        queue = deque()
        ones_count = 0
        for char in s:
            if char == "1":
                ones_count += 1
            queue.append(char)
            while ones_count > k:
                queue_char = queue.popleft()
                if queue_char == "1":
                    ones_count -= 1
            while queue and queue[0] == "0":
                queue.popleft()
            if ones_count == k:
                if len(queue) < len(min_substring):
                    min_substring = "".join(queue)
                elif len(queue) == len(min_substring):
                    possible_min_substring = "".join(queue)
                    if possible_min_substring < min_substring:
                        min_substring = possible_min_substring
        if len(min_substring) > n:
            return ""
        return min_substring
