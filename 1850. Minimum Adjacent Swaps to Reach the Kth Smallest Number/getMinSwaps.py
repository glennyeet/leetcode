class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        newNum = list(num)
        for _ in range(k):
            i = len(newNum) - 1
            while i > 0:
                if newNum[i - 1] < newNum[i]:
                    break
                i -= 1
            for j in range(len(newNum) - 1, i - 1, -1):
                if newNum[j] > newNum[i - 1]:
                    newNum[i - 1], newNum[j] = newNum[j], newNum[i - 1]
                    break
            newNum[i:] = reversed(newNum[i:])
        swaps = i = 0
        while i < len(num) - 1:
            if newNum[i] != num[i]:
                j = newNum.index(num[i], i + 1)
                newNum.insert(i, newNum.pop(j))
                swaps += j - i
            i += 1
        return swaps
