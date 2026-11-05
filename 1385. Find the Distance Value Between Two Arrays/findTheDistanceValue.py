class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        # Enumeration: O(m * n) time, O(1) space

        m = len(arr1)
        n = len(arr2)
        distance_value = 0
        for i in range(m):
            for j in range(n):
                if abs(arr1[i] - arr2[j]) <= d:
                    break
            else:
                distance_value += 1
        return distance_value
