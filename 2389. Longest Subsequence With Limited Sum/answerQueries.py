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

    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        self.mergeSort(nums)
        answer = []
        for query in queries:
            maxSize = total = i = 0
            while i < len(nums):
                total += nums[i]
                if total <= query:
                    maxSize += 1
                    i += 1
                else:
                    break
            answer.append(maxSize)
        return answer
