from collections import deque


class Solution:
    def robotWithString(self, s: str) -> str:
        # Greedy + Stack: O(n) time, O(n) space

        n = len(s)
        last_seen = [-1] * 26
        for i in range(n):
            last_seen[ord(s[i]) - ord("a")] = i
        s_pointer = 0
        t_stack = []
        smallest_string = []
        for i in range(26):
            char = chr(ord("a") + i)
            while t_stack and char >= t_stack[-1]:
                smallest_string.append(t_stack.pop())
            for j in range(s_pointer, last_seen[i] + 1):
                if s[j] == char:
                    smallest_string.append(s[j])
                else:
                    t_stack.append(s[j])
            s_pointer = max(s_pointer, last_seen[i] + 1)
        while t_stack:
            smallest_string.append(t_stack.pop())
        return "".join(smallest_string)
