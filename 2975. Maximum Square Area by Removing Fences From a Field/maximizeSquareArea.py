from typing import List


class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        # Hash Table + Enumeration: O(m^2 + n^2) time, O(m + n) space

        mod_factor = 10**9 + 7

        def get_side_lengths(fences: list[int]) -> set[int]:
            f = len(fences)
            side_lengths = set()
            for i in range(f):
                for j in range(i + 1, f):
                    side_lengths.add(abs(fences[i] - fences[j]))
            return side_lengths

        h_side_lengths = get_side_lengths(hFences + [1, m])
        v_side_lengths = get_side_lengths(vFences + [1, n])
        common_side_lengths = h_side_lengths.intersection(v_side_lengths)
        if not common_side_lengths:
            return -1
        else:
            return max(common_side_lengths) ** 2 % mod_factor
