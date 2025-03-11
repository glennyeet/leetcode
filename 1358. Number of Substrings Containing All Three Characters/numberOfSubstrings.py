class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Sliding window: O(n) time, O(1) space

        n = len(s)
        a_count = 0
        b_count = 0
        c_count = 0
        l = 0
        substrings = 0
        for r in range(n):
            if s[r] == "a":
                a_count += 1
            elif s[r] == "b":
                b_count += 1
            else:
                c_count += 1
            while a_count > 0 and b_count > 0 and c_count > 0:
                substrings += n - r
                if s[l] == "a":
                    a_count -= 1
                elif s[l] == "b":
                    b_count -= 1
                else:
                    c_count -= 1
                l += 1
        return substrings
