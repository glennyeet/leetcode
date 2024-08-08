class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        path = []
        totalCells = rows * cols
        currPos = [rStart, cStart]
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 0 right, 1 down, 2 left, 3 up
        currDir = 0
        ringLen = 1
        while totalCells > 0:
            for _ in range(2):
                for _ in range(ringLen):
                    if 0 <= currPos[0] < rows and 0 <= currPos[1] < cols:
                        path.append(currPos)
                        totalCells -= 1
                    currPos = [
                        currPos[0] + direction[currDir][0],
                        currPos[1] + direction[currDir][1],
                    ]
                currDir = (currDir + 1) % 4
            ringLen += 1
        return path
