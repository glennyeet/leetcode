from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        # Segment Tree + Hash Table: O(n * log(n)) time, O(n) space

        n = len(nums)
        mod_factor = 10**9 + 7
        sum_tree = [0] * (4 * n)
        squared_sum_tree = [0] * (4 * n)
        lazy_add = [0] * (4 * n)
        num_last_seen = {}
        result_sum = 0

        def range_add(
            node: int,
            left: int,
            right: int,
            query_left: int,
            query_right: int,
        ) -> None:
            if query_left <= left and right <= query_right:
                segment_length = right - left + 1
                squared_sum_tree[node] += 2 * sum_tree[node] + segment_length
                sum_tree[node] += segment_length
                lazy_add[node] += 1
                return
            mid = (left + right) // 2
            if lazy_add[node]:
                pending_add = lazy_add[node]
                for child_node, segment_left, segment_right in (
                    (2 * node, left, mid),
                    (2 * node + 1, mid + 1, right),
                ):
                    child_length = segment_right - segment_left + 1
                    squared_sum_tree[child_node] += (
                        2 * pending_add * sum_tree[child_node]
                        + pending_add**2 * child_length
                    )
                    sum_tree[child_node] += pending_add * child_length
                    lazy_add[child_node] += pending_add
                lazy_add[node] = 0
            if query_left <= mid:
                range_add(
                    2 * node,
                    left,
                    mid,
                    query_left,
                    query_right,
                )
            if query_right > mid:
                range_add(
                    2 * node + 1,
                    mid + 1,
                    right,
                    query_left,
                    query_right,
                )
            sum_tree[node] = sum_tree[2 * node] + sum_tree[2 * node + 1]
            squared_sum_tree[node] = (
                squared_sum_tree[2 * node] + squared_sum_tree[2 * node + 1]
            )

        for index, num in enumerate(nums):
            previous_index = num_last_seen.get(num, -1)
            range_add(
                1,
                0,
                n - 1,
                previous_index + 1,
                index,
            )
            num_last_seen[num] = index
            result_sum = (result_sum + squared_sum_tree[1]) % mod_factor
        return result_sum
