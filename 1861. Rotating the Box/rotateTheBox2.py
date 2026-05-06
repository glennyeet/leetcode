from typing import List


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # Simulation + Two Pointers: O(m * n) time, O(m * n) space

        m = len(boxGrid)
        n = len(boxGrid[0])
        rotated_box = [[""] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated_box[j][m - i - 1] = boxGrid[i][j]
        for j in range(m):
            lowest_cell = n - 1
            for i in reversed(range(n)):
                if rotated_box[i][j] == "#":
                    rotated_box[i][j] = "."
                    rotated_box[lowest_cell][j] = "#"
                    lowest_cell -= 1
                elif rotated_box[i][j] == "*":
                    lowest_cell = i - 1
        return rotated_box
