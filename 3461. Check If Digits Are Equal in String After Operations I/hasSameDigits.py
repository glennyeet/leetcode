class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # Simulation: O(n^2) time, O(n) space, where n is the size of s

        cur_s = list(s)
        while len(cur_s) > 2:
            new_s = []
            for i in range(len(cur_s) - 1):
                new_s.append(str((int(cur_s[i]) + int(cur_s[i + 1])) % 10))
            cur_s = new_s
        return cur_s[0] == cur_s[1]
