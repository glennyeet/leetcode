class Solution:
    def minSumSquareDiff(
        self, nums1: list[int], nums2: list[int], k1: int, k2: int
    ) -> int:
        # Greedy + Binary Search: O(n * log(m)) time, O(n) space,
        # where n is the size of nums1 and the size of nums2, and
        # m is max(deltas)

        deltas = []
        for num1, num2 in zip(nums1, nums2):
            deltas.append(abs(num1 - num2))
        k = k1 + k2

        def reductions_needed(target: int) -> int:
            used = 0
            for delta in deltas:
                if delta > target:
                    used += delta - target
            return used

        left = 0
        right = max(deltas)
        while left < right:
            mid = (left + right) // 2
            if reductions_needed(mid) <= k:
                right = mid
            else:
                left = mid + 1
        extra_reductions = k - reductions_needed(left)
        total = 0
        for delta in deltas:
            if delta > left:
                delta = left
            if delta == left and extra_reductions > 0 and delta > 0:
                delta -= 1
                extra_reductions -= 1
            total += delta**2
        return total
