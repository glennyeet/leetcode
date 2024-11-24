class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        ltr_lds = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    ltr_lds[i] = max(ltr_lds[i], 1 + ltr_lds[j])
        rtl_lds = [1] * n
        for i in range(n):
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    rtl_lds[i] = max(rtl_lds[i], 1 + rtl_lds[j])
        min_nums_ltr = [nums[0]] * n
        for i in range(1, n):
            min_nums_ltr[i] = min(min_nums_ltr[i - 1], nums[i])
        min_nums_rtl = [nums[n - 1]] * n
        for i in range(n - 2, -1, -1):
            min_nums_rtl[i] = min(min_nums_rtl[i + 1], nums[i])
        max_elements_kept = 1
        for i in range(1, n - 1):
            if min_nums_ltr[i - 1] < nums[i] and min_nums_rtl[i + 1] < nums[i]:
                max_elements_kept = max(max_elements_kept, ltr_lds[i] + rtl_lds[i] - 1)
        return n - max_elements_kept
