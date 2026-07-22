from bisect import bisect_right
from typing import List


class Solution:
    def maxActiveSectionsAfterTrade(
        self, s: str, queries: List[List[int]]
    ) -> List[int]:
        # Fenwick Tree + Binary Search: O((n + q) * log(n)) time, O(n + q) space

        n = len(s)
        active_sections = s.count("1")
        inactive_blocks = []
        i = 0
        while i < n:
            if s[i] == "0":
                start = i
                while i < n and s[i] == "0":
                    i += 1
                inactive_blocks.append((start, i - 1))
            else:
                i += 1
        m = len(inactive_blocks)
        inactive_block_starts = [a for a, _ in inactive_blocks]
        adjacent_zero_pairs = []
        for i in range(m - 1):
            left_block_start = inactive_blocks[i][0]
            right_block_end = inactive_blocks[i + 1][1]
            zeroes = (inactive_blocks[i][1] - inactive_blocks[i][0] + 1) + (
                inactive_blocks[i + 1][1] - inactive_blocks[i + 1][0] + 1
            )
            adjacent_zero_pairs.append((left_block_start, right_block_end, zeroes))
        adjacent_zero_pairs.sort(reverse=True)
        q = len(queries)
        query_order = sorted(range(q), key=lambda t: queries[t][0], reverse=True)
        fenwick_tree = [0] * (n + 1)

        def update(position: int, val: int) -> None:
            x = position + 1
            while x <= n:
                if val > fenwick_tree[x]:
                    fenwick_tree[x] = val
                x += x & -x

        def prefix_max(position: int) -> int:
            res = 0
            x = position + 1
            while x > 0:
                if fenwick_tree[x] > res:
                    res = fenwick_tree[x]
                x -= x & -x
            return res

        max_new_active_sections_from_full_pairs = [0] * q
        j = 0
        a = len(adjacent_zero_pairs)
        for i in query_order:
            l = queries[i][0]
            while j < a and adjacent_zero_pairs[j][0] >= l:
                update(adjacent_zero_pairs[j][1], adjacent_zero_pairs[j][2])
                j += 1
            max_new_active_sections_from_full_pairs[i] = prefix_max(queries[i][1])

        def inactive_block_containing(target: int) -> int:
            i = bisect_right(inactive_block_starts, target) - 1
            if i >= 0 and inactive_blocks[i][0] <= target <= inactive_blocks[i][1]:
                return i
            return -1

        answer = []
        for i in range(q):
            l, r = queries[i]
            max_new_active_sections = max_new_active_sections_from_full_pairs[i]
            if s[l] == "0":
                l_block = inactive_block_containing(l)
                if (
                    l_block != -1
                    and l > inactive_blocks[l_block][0]
                    and l_block + 1 < m
                ):
                    next_block_start = inactive_blocks[l_block + 1][0]
                    if r >= next_block_start:
                        l_len = inactive_blocks[l_block][1] - l + 1
                        r_len = (
                            min(inactive_blocks[l_block + 1][1], r)
                            - next_block_start
                            + 1
                        )
                        max_new_active_sections = max(
                            max_new_active_sections, l_len + r_len
                        )
            if s[r] == "0":
                r_block = inactive_block_containing(r)
                if (
                    r_block != -1
                    and r < inactive_blocks[r_block][1]
                    and r_block - 1 >= 0
                ):
                    prev_block_end = inactive_blocks[r_block - 1][1]
                    if l <= prev_block_end:
                        l_len = (
                            prev_block_end - max(inactive_blocks[r_block - 1][0], l) + 1
                        )
                        r_len = r - inactive_blocks[r_block][0] + 1
                        max_new_active_sections = max(
                            max_new_active_sections, l_len + r_len
                        )
            answer.append(active_sections + max_new_active_sections)
        return answer
