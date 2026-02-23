class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # Hash Table + Bit Manipulation: O(n * k) time,
        # O(n * k) space

        n = len(s)
        substrings = set()
        for i in range(n - k + 1):
            substrings.add(s[i : i + k])
        return len(substrings) == 2**k
