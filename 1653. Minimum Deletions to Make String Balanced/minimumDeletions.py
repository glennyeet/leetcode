class Solution:
    def minimumDeletions(self, s: str) -> int:
        # Prefix Sum: O(n) time, O(n) space, where n
        # is the size of s

        b_before = [0]
        total_b = 0
        for char in s:
            total_b += char == "b"
            b_before.append(total_b)
        a_after = [0]
        total_a = 0
        for char in reversed(s):
            total_a += char == "a"
            a_after.append(total_a)
        a_after.reverse()
        min_deletions = float("inf")
        for a, b in zip(a_after, b_before):
            min_deletions = min(min_deletions, a + b)
        return min_deletions
