class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # String: O(n^2) time, O(1) space

        n = len(s)
        for i in range(n):
            if s[i:] + s[:i] == goal:
                return True
        return False
