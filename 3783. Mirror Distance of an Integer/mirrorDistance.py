class Solution:
    def mirrorDistance(self, n: int) -> int:
        # Math: O(log(n)) time, O(1) space

        return abs(n - int(str(n)[::-1]))
