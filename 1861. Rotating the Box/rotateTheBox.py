class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        rotated_box = [[None] * m for _ in range(n)]
        for row in range(m):
            for col in range(n):
                rotated_box[col][m - row - 1] = box[row][col]
        for row in range(n - 1, -1, -1):
            for col in range(m):
                if rotated_box[row][col] == "#":
                    stone_row = row
                    while (
                        stone_row < n - 1
                        and rotated_box[stone_row + 1][col] != "#"
                        and rotated_box[stone_row + 1][col] != "*"
                    ):
                        stone_row += 1
                    rotated_box[row][col] = "."
                    rotated_box[stone_row][col] = "#"
        return rotated_box
