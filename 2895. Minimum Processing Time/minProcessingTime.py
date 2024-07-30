class Solution:
    def mergeSort(self, array: list[int]):
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

    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        sortedProcessorTime = processorTime
        self.mergeSort(sortedProcessorTime)
        sortedTasks = tasks
        self.mergeSort(sortedTasks)
        sortedTasks = list(reversed(sortedTasks))
        maxTimes = []
        for i in range(len(sortedProcessorTime)):
            pTime = sortedProcessorTime[i]
            t1Time = sortedTasks[i * 4]
            t2Time = sortedTasks[i * 4 + 1]
            t3Time = sortedTasks[i * 4 + 2]
            t4Time = sortedTasks[i * 4 + 3]
            maxTime = max(
                pTime + t1Time, pTime + t2Time, pTime + t3Time, pTime + t4Time
            )
            maxTimes.append(maxTime)
        minTime = max(maxTimes)
        return minTime
