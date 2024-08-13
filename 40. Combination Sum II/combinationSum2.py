class Solution:
    def partition(self, array: list[int], low: int, high: int) -> int:
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        i += 1
        array[i], array[high] = array[high], array[i]
        return i

    def quick_sort(self, array: list[int], low: int, high: int):
        if low < high:
            pi = self.partition(array, low, high)
            self.quick_sort(array, low, pi - 1)
            self.quick_sort(array, pi + 1, high)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combos = []
        n = len(candidates)
        # candidates.sort()
        self.quick_sort(candidates, 0, n - 1)

        def get_combo(index: int, target: int, combo: list[int]):
            if target == 0:
                combos.append(combo[:])
            elif index < n and target - candidates[index] >= 0:
                prev = -1
                for j in range(index, n):
                    if candidates[j] == prev:
                        continue
                    combo.append(candidates[j])
                    get_combo(j + 1, target - candidates[j], combo)
                    combo.pop()
                    prev = candidates[j]
            return

        get_combo(0, target, [])
        return combos
