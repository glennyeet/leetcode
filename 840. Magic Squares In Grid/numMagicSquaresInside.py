class Solution:
    def isMagicSquare(
        self, grid: list[list[int]], startRow: int, startCol: int
    ) -> bool:
        s1 = grid[startRow][startCol]
        s2 = grid[startRow][startCol + 1]
        s3 = grid[startRow][startCol + 2]
        s4 = grid[startRow + 1][startCol]
        s5 = grid[startRow + 1][startCol + 1]
        s6 = grid[startRow + 1][startCol + 2]
        s7 = grid[startRow + 2][startCol]
        s8 = grid[startRow + 2][startCol + 1]
        s9 = grid[startRow + 2][startCol + 2]
        sumR1 = s1 + s2 + s3
        sumR2 = s4 + s5 + s6
        sumR3 = s7 + s8 + s9
        sumC1 = s1 + s4 + s7
        sumC2 = s2 + s5 + s8
        sumC3 = s3 + s6 + s9
        sumD1 = s1 + s5 + s9
        sumD2 = s3 + s5 + s7
        sameSum = sumR1 == sumR2 == sumR3 == sumC1 == sumC2 == sumC3 == sumD1 == sumD2
        if not sameSum:
            return False
        nums = [s1, s2, s3, s4, s5, s6, s7, s8, s9]
        counter = {}
        for num in nums:
            if counter.get(num, 0) != 0 or not 1 <= num <= 9:
                return False
            counter[num] = 1
        return True

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if rows < 3 or cols < 3:
            return 0
        magicSquares = 0
        for i in range(rows - 3 + 1):
            for j in range(cols - 3 + 1):
                if self.isMagicSquare(grid, i, j):
                    magicSquares += 1
        return magicSquares
