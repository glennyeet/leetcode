class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Math: O(max(m, n)) time, O(max(m, n))
        # space, where m is the size of a and n
        # is the size of b

        return str(bin(int(a, 2) + int(b, 2)))[2:]
