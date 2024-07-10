class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        leftFurthest = rightFurthest = 0
        leftmostHouse = colors[0]
        for i in range(len(colors) - 1, -1, -1):
            if colors[i] != leftmostHouse:
                leftFurthest = i
                break
        rightmostHouse = colors[len(colors) - 1]
        for j in range(len(colors) - leftFurthest):
            if colors[j] != rightmostHouse:
                rightFurthest = len(colors) - 1 - j
                return rightFurthest
        return leftFurthest
