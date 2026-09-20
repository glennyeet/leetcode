class Solution:
    def reverseDegree(self, s: str) -> int:
        # Simulation: O(n) time, O(1) space, where n is the size of s

        reverse_degree = 0
        for i, char in enumerate(s):
            reverse_degree += (26 - (ord(char) - ord("a"))) * (i + 1)
        return reverse_degree
