class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0:
            if nums[i - 1] < nums[i]:
                break
            i -= 1
        if i == 0:
            k = len(nums) - 1
            while i < k:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
                k -= 1
            return nums
        j = len(nums) - 1
        while j > i - 1:
            if nums[j] > nums[i - 1]:
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                break
            j -= 1
        k = len(nums) - 1
        while i < k:
            nums[i], nums[k] = nums[k], nums[i]
            i += 1
            k -= 1
        return nums
