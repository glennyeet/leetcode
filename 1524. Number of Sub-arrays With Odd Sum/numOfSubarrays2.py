class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        # Prefix Sum + Math: O(n) time, O(1) space

        mod_factor = 10**9 + 7
        prefix_counts = [1, 0]  # even sum, odd sum
        prefix_parity = 0
        old_subarrays = 0
        for num in arr:
            prefix_parity = (prefix_parity + num) % 2
            old_subarrays += prefix_counts[(prefix_parity + 1) % 2]
            prefix_counts[prefix_parity] += 1
        return old_subarrays % mod_factor
