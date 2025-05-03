from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # Brute Force: O(n) time, O(1) space

        n = len(tops)

        def is_half_viable(num: int) -> bool:
            for i in range(n):
                if tops[i] != num and bottoms[i] != num:
                    return False
            return True

        tops_num = tops[0]
        bottoms_num = bottoms[0]
        tops_viable = is_half_viable(tops_num)
        bottoms_viable = is_half_viable(bottoms_num)
        if not tops_viable and not bottoms_viable:
            return -1

        def count_mismatches(half: List[int], target_num: int) -> int:
            mismatches = 0
            for i in range(n):
                mismatches += half[i] != target_num
            return mismatches

        min_rotations = float("inf")
        if tops_viable:
            tops_mismatches = count_mismatches(tops, tops_num)
            bottoms_mismatches = count_mismatches(bottoms, tops_num)
            min_rotations = min(min_rotations, tops_mismatches, bottoms_mismatches)
        if bottoms_viable:
            tops_mismatches = count_mismatches(tops, bottoms_num)
            bottoms_mismatches = count_mismatches(bottoms, bottoms_num)
            min_rotations = min(min_rotations, tops_mismatches, bottoms_mismatches)
        return min_rotations
