class Solution:
    def mergeSort(self, array: list[str], counter: dict[str, int]):
        if len(array) > 1:
            m = len(array) // 2
            L = array[:m]
            R = array[m:]
            self.mergeSort(L, counter)
            self.mergeSort(R, counter)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if counter.get(L[i]) >= counter.get(R[j]):
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

    def minimumPushes(self, word: str) -> int:
        counter = {}
        for char in word:
            counter[char] = counter.get(char, 0) + 1
        letters = list(set(word))
        self.mergeSort(letters, counter)
        pushes = 0
        remaps = 0
        for i in range(len(letters)):
            if i % 8 == 0:
                remaps += 1
            pushes += counter.get(letters[i]) * remaps
        return pushes
