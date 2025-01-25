from collections import deque


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # Greedy: O(nlog(n)) time, O(n) space, where n is the size of nums

        sorted_nums = nums.copy()
        sorted_nums.sort()
        groups = []
        num_to_group = {}
        for num in sorted_nums:
            if not groups or abs(groups[-1][-1] - num) > limit:
                groups.append(deque([num]))
            else:
                groups[-1].append(num)
            num_to_group[num] = len(groups) - 1
        smallest_array = []
        for num in nums:
            smallest_array.append(groups[num_to_group[num]].popleft())
        return smallest_array
