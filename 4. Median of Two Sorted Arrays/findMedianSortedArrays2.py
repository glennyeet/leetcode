class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = (m + n + 1) // 2 - mid1
            maxLeft1 = float("-inf") if mid1 - 1 < 0 else nums1[mid1 - 1]
            minRight1 = float("inf") if mid1 >= m else nums1[mid1]
            maxLeft2 = float("-inf") if mid2 - 1 < 0 else nums2[mid2 - 1]
            minRight2 = float("inf") if mid2 >= n else nums2[mid2]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                high = mid1 - 1
            else:
                low = mid1 + 1
