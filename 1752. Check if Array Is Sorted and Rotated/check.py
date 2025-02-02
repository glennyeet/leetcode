class Solution:
    def check(self, nums: List[int]) -> bool:
        # Brute force: O(n) time, O(1) space

        n = len(nums)
        sorted_nums = 1
        for i in range(1, 2 * n):
            if nums[(i - 1) % n] <= nums[i % n]:
                sorted_nums += 1
            else:
                sorted_nums = 1
            if sorted_nums == n:
                return True
        return n == 1
