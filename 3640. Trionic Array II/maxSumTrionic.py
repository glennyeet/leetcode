from typing import List


class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        # Kadane's Algorithm: O(n) time, O(n) space

        n = len(nums)
        p = None
        p_to_q_chunks = []
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                if p is None:
                    p = i
            else:
                if p is not None:
                    p_to_q_chunks.append((p, i))
                    p = None

        def find_max_strictly_increasing_sum(start_index: int, delta: int) -> int:
            i = start_index
            chunk_sum = 0
            max_chunk_sum = float("-inf")
            if delta == -1:
                cmp = lambda a, b: a > b
            else:
                cmp = lambda a, b: a < b
            while 0 < i < n - 1 and cmp(nums[i], nums[i + delta]):
                i += delta
                chunk_sum += nums[i]
                max_chunk_sum = max(max_chunk_sum, chunk_sum)
            return max_chunk_sum

        max_sum = float("-inf")
        for p, q in p_to_q_chunks:
            if p == 0 or q == n - 1:
                continue
            p_to_q_sum = sum(nums[p : q + 1])
            max_l_to_p_sum = find_max_strictly_increasing_sum(p, -1)
            max_q_to_r_sum = find_max_strictly_increasing_sum(q, 1)
            max_sum = max(max_sum, max_l_to_p_sum + p_to_q_sum + max_q_to_r_sum)
        return max_sum
