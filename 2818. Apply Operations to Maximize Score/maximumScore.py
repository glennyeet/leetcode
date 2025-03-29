from typing import List
from math import sqrt
from heapq import heapify, heappop


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # Stack + Priority queue: O(n * sqrt(m) + klog(n))
        # time, O(n) space, where m is any value in nums

        n = len(nums)
        max_score = 1
        prime_scores = []
        for num in nums:
            score = 0
            for possible_factor in range(2, int(sqrt(num)) + 1):
                if num % possible_factor == 0:
                    score += 1
                    while num % possible_factor == 0:
                        num //= possible_factor
            if num >= 2:
                score += 1
            prime_scores.append(score)
        left_bound = [-1] * n
        right_bound = [n] * n
        stack = []
        for i, score in enumerate(prime_scores):
            while stack and prime_scores[stack[-1]] < score:
                stack_index = stack.pop()
                right_bound[stack_index] = i
            if stack:
                left_bound[i] = stack[-1]
            stack.append(i)
        max_heap = []
        for i, num in enumerate(nums):
            max_heap.append((-num, i))
        heapify(max_heap)
        k_remaining = k
        mod = 10**9 + 7
        while k_remaining:
            num, i = heappop(max_heap)
            num = -num
            score = prime_scores[i]
            left_count = i - left_bound[i]
            right_count = right_bound[i] - i
            count = left_count * right_count
            operations = min(k_remaining, count)
            k_remaining -= operations
            max_score = max_score * pow(num, operations, mod) % mod
        return max_score
