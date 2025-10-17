from functools import cache


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        # Top-down DP: O(n) time, O(n) space

        n = len(s)
        s_bitmasks = []
        for i in range(n):
            s_bitmasks.append(1 << ord(s[i]) - ord("a"))

        @cache
        def find_max_partitions(
            start_index: int, used_change_operation: bool, char_bitmask: int
        ):
            if start_index == n:
                return 1
            max_partitions = 0
            ones_count = char_bitmask.bit_count()
            if not char_bitmask & s_bitmasks[start_index]:
                if ones_count + 1 <= k:
                    max_partitions = find_max_partitions(
                        start_index + 1,
                        used_change_operation,
                        char_bitmask | s_bitmasks[start_index],
                    )
                else:
                    max_partitions = (
                        find_max_partitions(
                            start_index + 1,
                            used_change_operation,
                            s_bitmasks[start_index],
                        )
                        + 1
                    )
            else:
                max_partitions = find_max_partitions(
                    start_index + 1, used_change_operation, char_bitmask
                )
            if not used_change_operation:
                for i in range(26):
                    letter_bitmask = 1 << i
                    if not char_bitmask & letter_bitmask:
                        if ones_count + 1 <= k:
                            max_partitions = max(
                                max_partitions,
                                find_max_partitions(
                                    start_index + 1,
                                    True,
                                    char_bitmask | letter_bitmask,
                                ),
                            )
                        else:
                            max_partitions = max(
                                max_partitions,
                                find_max_partitions(
                                    start_index + 1,
                                    True,
                                    letter_bitmask,
                                )
                                + 1,
                            )
                    else:
                        max_partitions = max(
                            max_partitions,
                            find_max_partitions(start_index + 1, True, char_bitmask),
                        )
            return max_partitions

        return find_max_partitions(0, False, 0)
