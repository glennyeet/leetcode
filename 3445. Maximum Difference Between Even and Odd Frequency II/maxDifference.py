from collections import deque


class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        # Sliding Window + Prefix Sum + Queue: O(n) time, O(n) space

        chars_set = set(s)
        s2 = s + "5"
        n = len(s2)
        max_difference = float("-inf")
        for odd_char in chars_set:
            for even_char in chars_set:
                if odd_char == even_char:
                    continue
                odd_count = 0
                even_count = 0
                min_poc_minus_pec = [float("inf")] * 4
                counts_queue = deque([(k - 1, 0, 0)])
                for i in range(n):
                    counts_queue.append((i + k, odd_count, even_count))
                    if s2[i] == odd_char:
                        odd_count += 1
                    elif s2[i] == even_char:
                        even_count += 1
                    while counts_queue and counts_queue[0][0] <= i:
                        _, prev_odd_count, prev_even_count = counts_queue[0]
                        if prev_even_count == even_count:
                            break
                        mpmp_index = prev_odd_count % 2 * 2 + prev_even_count % 2
                        min_poc_minus_pec[mpmp_index] = min(
                            min_poc_minus_pec[mpmp_index],
                            prev_odd_count - prev_even_count,
                        )
                        counts_queue.popleft()
                    mpmp_index = (odd_count + 1) % 2 * 2 + even_count % 2
                    if i + 1 >= k:
                        max_difference = max(
                            max_difference,
                            odd_count - even_count - min_poc_minus_pec[mpmp_index],
                        )
        return max_difference
