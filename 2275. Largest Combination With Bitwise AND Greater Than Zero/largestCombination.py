class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        sizes = [0] * 32
        for num in candidates:
            for i in range(32):
                if num & 1 << i > 0:
                    sizes[i] += 1
        return max(sizes)
