class Solution:
    def largestOddNumber(self, num: str) -> str:
        largestInt = ""
        i = len(num) - 1
        while i >= 0 and largestInt == "":
            if int(num[i]) % 2 == 1:
                largestInt = num[0 : i + 1]
            i -= 1
        return largestInt
