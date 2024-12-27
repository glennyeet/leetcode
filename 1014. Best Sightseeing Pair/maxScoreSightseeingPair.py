class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # Bottom-up DP: O(n) time, O(1) space

        max_value = values[0] - 1
        max_score = 0
        for i in range(1, len(values)):
            max_score = max(max_score, max_value + values[i])
            max_value = max(max_value - 1, values[i] - 1)
        return max_score
