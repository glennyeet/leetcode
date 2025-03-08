class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Sliding window: O(n) time, O(1) space

        n = len(blocks)
        white_blocks = 0
        black_blocks = 0
        i = 0
        min_operations = float("inf")
        for j in range(n):
            if blocks[j] == "W":
                white_blocks += 1
            else:
                black_blocks += 1
            if j - i + 1 > k:
                if blocks[i] == "W":
                    white_blocks -= 1
                else:
                    black_blocks -= 1
                i += 1
            if j - i + 1 == k:
                min_operations = min(min_operations, white_blocks)
        return min_operations
