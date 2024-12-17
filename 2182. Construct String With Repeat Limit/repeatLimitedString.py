from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        largest_string = []
        counter = Counter(s)
        p_queue = []
        for char in counter:
            p_queue.append((-ord(char), counter[char]))
        heapify(p_queue)
        while p_queue:
            neg_unicode, count = heappop(p_queue)
            for _ in range(min(count, repeatLimit)):
                largest_string.append(chr(-neg_unicode))
            if count > repeatLimit:
                if not p_queue:
                    break
                second_neg_unicode, second_count = heappop(p_queue)
                largest_string.append(chr(-second_neg_unicode))
                second_count -= 1
                if second_count:
                    heappush(p_queue, (second_neg_unicode, second_count))
                heappush(p_queue, (neg_unicode, count - repeatLimit))
        return "".join(largest_string)
