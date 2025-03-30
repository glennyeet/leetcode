from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Two Pointers: O(n) time, O(n) space

        # Version 1

        # s = list(s)
        # lastSeen = {}
        # for i in range(len(s)):
        #     lastSeen[s[i]] = i
        # partitionSizes = []
        # i = j = 0
        # while i < len(s):
        #     j = lastSeen[s[i]]
        #     k = 0
        #     while k < j:
        #         if lastSeen[s[k]] > j:
        #             j = lastSeen[s[k]]
        #         k += 1
        #     partitionSizes.append(j - i + 1)
        #     i = j + 1
        # return partitionSizes

        # Version 2

        n = len(s)
        last_seen = {}
        for start_index, c in enumerate(s):
            last_seen[c] = start_index
        partition_sizes = []
        start_index = 0
        while start_index < n:
            last_seen_index = last_seen[s[start_index]]
            i = start_index + 1
            while i < last_seen_index:
                new_last_seen_index = last_seen[s[i]]
                if new_last_seen_index > last_seen_index:
                    last_seen_index = new_last_seen_index
                i += 1
            partition_sizes.append(last_seen_index - start_index + 1)
            start_index = last_seen_index + 1
        return partition_sizes
