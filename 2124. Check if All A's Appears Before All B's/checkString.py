class Solution:
    def checkString(self, s: str) -> bool:
        # String: O(n) time, O(1) space,
        # where n is the size of s

        b_seen = False
        for char in s:
            if not b_seen:
                b_seen = char == "b"
            if char == "a" and b_seen:
                return False
        return True
