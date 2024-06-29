class Solution(object):
    def dfs(self, image, sr, sc, oldColour, newColour):
        if (
            sr < 0
            or sr >= len(image)
            or sc < 0
            or sc >= len(image[0])
            or image[sr][sc] != oldColour
        ):
            return
        image[sr][sc] = newColour
        self.dfs(image, sr + 1, sc, oldColour, newColour)
        self.dfs(image, sr - 1, sc, oldColour, newColour)
        self.dfs(image, sr, sc + 1, oldColour, newColour)
        self.dfs(image, sr, sc - 1, oldColour, newColour)

    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == color:
            return image
        self.dfs(image, sr, sc, image[sr][sc], color)
        return image
