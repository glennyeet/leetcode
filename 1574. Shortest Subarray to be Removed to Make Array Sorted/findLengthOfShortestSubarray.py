class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        shortest_len = right
        left = 0
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1
        shortest_len = min(shortest_len, n - left - 1)
        left = 0
        right = n - 1
        while left < right:
            while (
                right < n
                and left + 1 < right
                and arr[right - 1] <= arr[right]
                and arr[left] <= arr[right]
            ):
                right -= 1
            while right < n and arr[left] > arr[right]:
                right += 1
            shortest_len = min(shortest_len, right - left - 1)
            if arr[left] > arr[left + 1]:
                break
            left += 1

        return shortest_len
