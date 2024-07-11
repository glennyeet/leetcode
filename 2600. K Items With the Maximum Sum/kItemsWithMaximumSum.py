class Solution:
    def kItemsWithMaximumSum(
        self, numOnes: int, numZeros: int, numNegOnes: int, k: int
    ) -> int:
        if k > numOnes + numZeros:
            maxSum = min(numOnes, k)
            k -= numOnes + numZeros
            maxSum -= min(numNegOnes, k)
        else:
            maxSum = min(numOnes, k)
        return maxSum
