class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        maxNumber = ""
        for i in range(len(number)):
            if number[i] == digit:
                result = number[0:i] + number[i + 1 : len(number)]
                if result > maxNumber:
                    maxNumber = result
        return maxNumber
