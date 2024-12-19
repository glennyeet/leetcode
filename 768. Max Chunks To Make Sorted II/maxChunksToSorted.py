class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # Use sort() and enumerate()

        sorted_arr = arr.copy()
        sorted_arr.sort()
        expected_prefix_sum = 0
        actual_prefix_sum = 0
        max_chunks = 0
        for i, num in enumerate(arr):
            expected_prefix_sum += sorted_arr[i]
            actual_prefix_sum += num
            if expected_prefix_sum == actual_prefix_sum:
                max_chunks += 1
        return max_chunks

        # Use sorted() and zip()

        # expected_prefix_sum = 0
        # actual_prefix_sum = 0
        # max_chunks = 0
        # for sorted_num, unsorted_num in zip(sorted(arr), arr):
        #     expected_prefix_sum += sorted_num
        #     actual_prefix_sum += unsorted_num
        #     if expected_prefix_sum == actual_prefix_sum:
        #         max_chunks += 1
        # return max_chunks
