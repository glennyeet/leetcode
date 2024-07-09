class Solution:
    def mergeSort(self, array):
        if len(array) > 1:
            m = len(array) // 2
            L = array[:m]
            R = array[m:]
            self.mergeSort(L)
            self.mergeSort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                array[k] = R[j]
                j += 1
                k += 1

    def splitNum(self, num: int) -> int:
        digits = [digit for digit in str(num)]
        self.mergeSort(digits)
        num1 = []
        num2 = []
        for i in range(len(digits)):
            if i % 2 == 0:
                num1.append(digits[i])
            else:
                num2.append(digits[i])
        minSum = int(''.join(num1)) + int(''.join(num2))
        return minSum
