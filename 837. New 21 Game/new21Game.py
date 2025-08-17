class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Bottom-up DP + Sliding Window: O(n + m) time,
        # O(n + m) space, where m is maxPts

        probabilities = [0.0] * (n + maxPts + 1)
        for i in range(k, n + 1):
            probabilities[i] = 1.0
        numerator = sum(probabilities[k + 1 : k + maxPts + 1])
        for i in reversed(range(k)):
            numerator -= probabilities[i + maxPts + 1]
            numerator += probabilities[i + 1]
            probabilities[i] = numerator / maxPts
        return probabilities[0]
