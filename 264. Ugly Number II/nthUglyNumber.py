import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = set([1])
        heap = [1]
        for _ in range(n - 1):
            ugly_number = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                new_ugly_number = ugly_number * factor
                if new_ugly_number not in ugly_numbers:
                    ugly_numbers.add(new_ugly_number)
                    heapq.heappush(heap, new_ugly_number)
        answer = heap[0]
        return answer
