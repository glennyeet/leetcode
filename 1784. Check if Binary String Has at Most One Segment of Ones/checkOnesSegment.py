class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # String: O(n) time, O(1) space

        n = len(s)
        has_segment = True
        for i in range(1, n):
            if s[i] == "0":
                if has_segment:
                    has_segment = False
            elif s[i] == "1" and has_segment:
                continue
            else:
                return False
        return True
