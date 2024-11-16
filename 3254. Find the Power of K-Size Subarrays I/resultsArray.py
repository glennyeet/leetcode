class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # Brute force O(nk) time O(1) space

        # powers = []
        # for i in range(len(nums) - k + 1):
        #     power = nums[i]
        #     for j in range(i + 1, i + k):
        #         if nums[j - 1] + 1 != nums[j]:
        #             power = -1
        #             break
        #         else:
        #             power = max(power, nums[j])
        #     powers.append(power)
        # return powers

        # Sliding window O(n) time O(1) space

        powers = []
        i = 0
        j = 0
        consecutive = 0
        while j < k:
            if i == j or nums[j - 1] + 1 == nums[j]:
                consecutive += 1
            j += 1
        j -= 1
        while j < len(nums):
            if consecutive == k:
                powers.append(nums[j])
            else:
                powers.append(-1)
            j += 1
            if j == len(nums):
                break
            i += 1
            if nums[i - 1] + 1 == nums[i]:
                consecutive -= 1
            if nums[j - 1] + 1 == nums[j]:
                consecutive += 1
        return powers

        # Sliding window 2 O(n) time O(1) space

        # powers = []
        # i = 0
        # consecutive = 1
        # for j in range(len(nums)):
        #     if j > 0 and nums[j - 1] + 1 == nums[j]:
        #         consecutive += 1
        #     if j - i + 1 > k:
        #         if nums[i] + 1 == nums[i + 1]:
        #             consecutive -= 1
        #         i += 1
        #     if j - i + 1 == k:
        #         if consecutive == k:
        #             powers.append(nums[j])
        #         else:
        #             powers.append(-1)
        # return powers
