from sortedcontainers import SortedList
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        # Sliding Window + Bottom-up DP: O(n * log(x) + n * k) time, O(n * k) space

        n = len(nums)
        medians = [0] * n
        subarray_operations = [0] * n
        sorted_list = SortedList()
        for i in range(n):
            if i >= x:
                removed_idx = i - x
                sorted_list.remove(nums[i - x])
            sorted_list.add(nums[i])
            if i >= x - 1:
                medians[i] = sorted_list[x // 2]
                if i == x - 1:
                    operations = 0
                    for j in range(x):
                        operations += abs(medians[i] - nums[j])
                else:
                    prev_operations = subarray_operations[i - 1]
                    if medians[i] == medians[i - 1]:
                        operations = (
                            prev_operations
                            + abs(nums[i] - medians[i])
                            - abs(nums[removed_idx] - medians[i - 1])
                        )
                    elif medians[i] > medians[i - 1]:
                        operations = (
                            prev_operations
                            + abs(nums[i] - medians[i - 1])
                            - abs(nums[removed_idx] - medians[i - 1])
                        )
                        delta = medians[i] - medians[i - 1]
                        operations += (x // 2 - 1) * delta - (x - x // 2 - 1) * delta
                    else:
                        operations = (
                            prev_operations
                            + abs(nums[i] - medians[i - 1])
                            - abs(nums[removed_idx] - medians[i - 1])
                        )
                        delta = medians[i - 1] - medians[i]
                        operations += (x - 1 - x // 2 - 1) * delta - (x // 2) * delta
                subarray_operations[i] = operations
        dp = [[float("inf")] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(k + 1):
                if j == 0 or i == 0:
                    dp[i][j] = 0
                    continue
                if j * x > i:
                    break
                skip = dp[i - 1][j]
                last_available_idx = i - x
                take = subarray_operations[i - 1] + dp[last_available_idx][j - 1]
                dp[i][j] = min(skip, take)
        return dp[n][k]
