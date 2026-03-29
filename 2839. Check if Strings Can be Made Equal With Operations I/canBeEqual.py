class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # String: O(1) time, O(1) space

        n = len(s1)
        if s1 == s2:
            return True
        new_s1 = list(s1)
        for i in range(n):
            j = i + 2
            if j < n and s1[i] == s2[j] and s1[j] == s2[i]:
                new_s1[i], new_s1[j] = new_s1[j], new_s1[i]
                if "".join(new_s1) == s2:
                    return True
        return False
