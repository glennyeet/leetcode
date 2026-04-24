class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # String: O(n) time, O(1) space

        n = len(moves)
        l_count = 0
        r_count = 0
        for move in moves:
            l_count += move == "L"
            r_count += move == "R"
        blank_count = n - l_count - r_count
        return abs(l_count - r_count) + blank_count
