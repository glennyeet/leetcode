class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed) and n > 0:
            if i - 1 < 0:
                leftValid = True
            else:
                leftValid = flowerbed[i - 1] == 0
            if i + 1 > len(flowerbed) - 1:
                rightValid = True
            else:
                rightValid = flowerbed[i + 1] == 0
            if flowerbed[i] == 0 and leftValid and rightValid:
                flowerbed[i] = 1
                n -= 1
            i += 1
        return n == 0
