class Solution:
    def minChanges(self, s: str) -> int:
        # Greedy: O(n) time, O(1) space

        n = len(s)
        min_changes = 0
        for i in range(1, n, 2):
            min_changes += s[i - 1] != s[i]
        return min_changes
