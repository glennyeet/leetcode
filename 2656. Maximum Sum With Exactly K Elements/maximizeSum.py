class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        max_score = 0
        for i in range(k):
            max_score += max_num + i
        return max_score
