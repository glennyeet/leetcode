from collections import Counter


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        interval_counter = Counter()
        for left, right in intervals:
            interval_counter[left] += 1
            interval_counter[right + 1] -= 1
        overlap = 0
        max_overlap = 0
        for num in sorted(interval_counter):
            overlap += interval_counter[num]
            max_overlap = max(max_overlap, overlap)
        groups = max_overlap
        return groups
