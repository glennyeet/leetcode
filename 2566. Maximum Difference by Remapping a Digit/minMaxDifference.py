class Solution:
    def minMaxDifference(self, num: int) -> int:
        numString = str(num)
        digitToMapMax = None
        digitToMapMin = numString[0]
        maxNum = list(numString)
        minNum = list(numString)
        for i in range(len(numString)):
            if numString[i] != "9":
                digitToMapMax = numString[i]
                break
        for i in range(len(numString)):
            if numString[i] == digitToMapMin:
                minNum[i] = '0'
        if digitToMapMax:
            for i in range(len(maxNum)):
                if maxNum[i] == digitToMapMax:
                    maxNum[i] = "9"
        diff = int("".join(maxNum)) - int("".join(minNum))
        return diff
