class Solution:
    def coloredCells(self, n: int) -> int:
        # Brute force: O(n) time, O(1) space

        colored_cells = 1
        for i in range(n):
            colored_cells += 4 * i
        return colored_cells
