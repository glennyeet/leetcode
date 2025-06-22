from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        # Brute Force: O(n) time, O(n) space

        n = len(s)
        groups = []
        for i in range(0, n, k):
            if i + k > n:
                groups.append(s[i:] + fill * (i + k - n))
            else:
                groups.append(s[i : i + k])
        return groups
