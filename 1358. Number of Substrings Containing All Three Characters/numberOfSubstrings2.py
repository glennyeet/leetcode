class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # String: O(n) time, O(n) space

        n = len(s)
        first_a = []
        first_b = []
        first_c = []
        next_a = n
        next_b = n
        next_c = n
        for i in reversed(range(n)):
            if s[i] == "a":
                next_a = i
            elif s[i] == "b":
                next_b = i
            elif s[i] == "c":
                next_c = i
            first_a.append(next_a)
            first_b.append(next_b)
            first_c.append(next_c)
        valid_substrings = 0
        for i in range(n):
            valid_substrings += n - max(first_a[i], first_b[i], first_c[i])
        return valid_substrings
