class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        area = 0
        prevRowHeights = []
        for i in range(len(matrix)):
            currRowHeights = []
            streak = [False] * len(matrix[0])
            for j in range(len(prevRowHeights)):
                streak[prevRowHeights[j][1]] = True
                if matrix[i][prevRowHeights[j][1]] == 1:
                    currRowHeights.append(
                        (prevRowHeights[j][0] + 1, prevRowHeights[j][1])
                    )
            for k in range(len(matrix[0])):
                if matrix[i][k] == 1:
                    if streak[k] == False:
                        currRowHeights.append((1, k))
            for l in range(len(currRowHeights)):
                area = max((l + 1) * currRowHeights[l][0], area)
            prevRowHeights = currRowHeights
        return area
