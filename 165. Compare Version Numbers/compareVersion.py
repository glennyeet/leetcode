class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Two Pointers: O(max(m, n)) time, O(m + n) space

        revisions1 = version1.split(".")
        m = len(revisions1)
        revisions2 = version2.split(".")
        n = len(revisions2)
        if m > n:
            revisions2.extend(["0"] * (m - n))
        elif n > m:
            revisions1.extend(["0"] * (n - m))
        for r1, r2 in zip(revisions1, revisions2):
            if int(r1) > int(r2):
                return 1
            elif int(r1) < int(r2):
                return -1
        return 0
