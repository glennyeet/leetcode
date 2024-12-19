class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        expected_prefix_sum = 0
        actual_prefix_sum = 0
        max_chunks = 0
        for i, num in enumerate(arr):
            expected_prefix_sum += i
            actual_prefix_sum += num
            if expected_prefix_sum == actual_prefix_sum:
                max_chunks += 1
        return max_chunks
