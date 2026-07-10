from bisect import bisect_right
from typing import List


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[int]:
        # Binary Lifting: O(n * log(n) + q * log(n)) time, O(q) space, where 
        # q is the size of queries

        max_jump_power = 20
        sorted_nums = sorted(nums)
        dp = [{} for _ in range(max_jump_power + 1)]
        for i in range(n):
            dp[0][sorted_nums[i]] = sorted_nums[i]
            j = bisect_right(sorted_nums, sorted_nums[i] + maxDiff) - 1
            dp[1][sorted_nums[i]] = sorted_nums[j]
        for d in range(2, max_jump_power):
            for i in dp[d - 1]:
                j = dp[d - 1][i]
                dp[d][i] = dp[d - 1][j]
        answer = []
        for u, v in queries:
            if u == v:
                answer.append(0)
            else:
                a = nums[u]
                b = nums[v]
                if a > b:
                    a, b = b, a
                if a == b:
                    answer.append(1)
                elif dp[max_jump_power - 1][a] < b:
                    answer.append(-1)
                else:
                    jumps = 0
                    cur_node = a
                    for i in reversed(range(1, max_jump_power)):
                        if dp[i][cur_node] < b:
                            cur_node = dp[i][cur_node]
                            jumps += 1 << i - 1
                    answer.append(jumps + 1)
        return answer
