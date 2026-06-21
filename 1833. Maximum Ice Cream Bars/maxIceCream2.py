from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Greedy + Counting Sort: O(n * log(n)) time, O(n + c)
        # space, where n is the size of costs and c is
        # max(costs)

        def counting_sort(nums: list[int]) -> list[int]:
            counts = [0] * (max(nums) + 1)
            for num in nums:
                counts[num] += 1
            prefix_sum = []
            cur_sum = 0
            for count in counts:
                cur_sum += count
                prefix_sum.append(cur_sum)
            ans = [0] * len(nums)
            for num in reversed(nums):
                ans[prefix_sum[num] - 1] = num
                prefix_sum[num] -= 1
            return ans

        sorted_costs = counting_sort(costs)
        coins_used = 0
        max_ice_cream_bars = 0
        for cost in sorted_costs:
            coins_used += cost
            max_ice_cream_bars += coins_used <= coins
        return max_ice_cream_bars
