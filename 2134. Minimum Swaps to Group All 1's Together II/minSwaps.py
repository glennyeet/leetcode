class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        onesCount = 0
        for num in nums:
            if num == 1:
                onesCount += 1
        minSwaps = 0
        i = 0
        while i < onesCount:
            if nums[i] == 0:
                minSwaps += 1
            i += 1
        initSwaps = minSwaps
        flatSwaps = minSwaps
        i = 0
        j = onesCount - 1
        while j < len(nums) - 1:
            if nums[i] == 0:
                flatSwaps -= 1
            i += 1
            j += 1
            if nums[j] == 0:
                flatSwaps += 1
            minSwaps = min(flatSwaps, minSwaps)
        circleSwaps = initSwaps
        i = len(nums)
        j = onesCount - 1
        while j > 0:
            if nums[j] == 0:
                circleSwaps -= 1
            j -= 1
            i -= 1
            if nums[i] == 0:
                circleSwaps += 1
            minSwaps = min(circleSwaps, minSwaps)
        return minSwaps
