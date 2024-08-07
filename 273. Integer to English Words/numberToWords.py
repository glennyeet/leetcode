class Solution:
    d = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion",
    }

    def getHundredsNumber(self, num: int) -> str:
        if num == 0:
            return ""
        elif num <= 20:
            return self.d[num] + " "
        numString = ""
        numCopy = num
        if numCopy // 100 > 0:
            numString += self.d[numCopy // 100] + " " + self.d[100] + " "
        numCopy %= 100
        if numCopy == 0:
            return numString
        elif numCopy <= 20 or numCopy > 20 and numCopy % 10 == 0:
            numString += self.d[numCopy] + " "
        else:
            numString += self.d[numCopy // 10 * 10] + " " + self.d[numCopy % 10] + " "
        return numString

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return self.d[0]
        numString = ""
        numCopy = num
        exp = 3
        while numCopy > 0:
            remainder = numCopy % 1000
            numCopy //= 1000
            numString = self.getHundredsNumber(remainder) + numString
            if numCopy > 0 and numCopy % 1000 != 0:
                numString = self.d[10**exp] + " " + numString
            exp += 3
        numString = numString.strip()
        return numString
