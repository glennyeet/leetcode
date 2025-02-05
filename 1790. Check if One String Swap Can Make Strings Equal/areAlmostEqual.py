class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # One-pass: O(n) time, O(1) space

        if s1 == s2:
            return True
        diff_chars1 = []
        diff_chars2 = []
        for char1, char2 in zip(s1, s2):
            if char1 != char2:
                diff_chars1.append(char1)
                diff_chars2.append(char2)
            if len(diff_chars1) > 2:
                return False
        for char in diff_chars1:
            if char not in diff_chars2:
                return False
        return True
