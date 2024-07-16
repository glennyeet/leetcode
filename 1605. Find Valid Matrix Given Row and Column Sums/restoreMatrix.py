class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        result = [[0] * len(colSum) for _ in range(len(rowSum))]
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                minNum = min(rowSum[i], colSum[j])
                result[i][j] = minNum
                rowSum[i] -= minNum
                colSum[j] -= minNum
        return result
