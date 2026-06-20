from typing import List


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # Stack + Binary Search: O(r * log(r) + r * log(u)) time, O(r)
        # space, where r is the size of restrictions and u is the size
        # of restricton's universe

        sorted_restrictions = sorted(restrictions)
        if not sorted_restrictions or sorted_restrictions[-1][0] < n:
            sorted_restrictions.append((n, n))
        stack = []
        for cur_id, cur_max_height in sorted_restrictions:
            while stack:
                prev_id, prev_max_height = stack[-1]
                if (
                    prev_max_height > cur_max_height
                    and cur_id - prev_id < prev_max_height - cur_max_height
                ):
                    stack.pop()
                else:
                    break
            stack.append((cur_id, cur_max_height))

        def find_max_delta(delta_id: int, delta_max_height: int) -> int:
            left = 0
            right = 10**9
            while left < right:
                mid = (left + right + 1) // 2
                cost = mid + max(0, mid - delta_max_height)
                if cost <= delta_id:
                    left = mid
                else:
                    right = mid - 1
            return left

        prev_id = 1
        prev_max_height = 0
        max_height = 0
        for cur_id, cur_max_height in stack:
            delta_id = cur_id - prev_id
            delta_max_height = cur_max_height - prev_max_height
            if abs(delta_max_height) > delta_id:
                if delta_max_height > 0:
                    delta_max_height = min(delta_max_height, delta_id)
                else:
                    delta_max_height = max(delta_max_height, delta_id)
            max_delta = find_max_delta(delta_id, delta_max_height)
            max_height = max(max_height, max_delta + prev_max_height)
            prev_id = cur_id
            prev_max_height += delta_max_height
        return max_height
