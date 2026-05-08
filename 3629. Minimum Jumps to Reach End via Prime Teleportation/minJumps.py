from typing import List
from collections import defaultdict, deque


def sieve_of_eratosthenes(max_num: int) -> list[int]:
    primes = [i for i in range(max_num + 1)]
    primes[0] = primes[1] = -1
    for i in range(2, max_num + 1):
        if primes[i] == i:
            j = i**2
            while j <= max_num:
                primes[j] = i
                j += i
    return primes


primes = sieve_of_eratosthenes(10**6)


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        # Math + BFS: O(m * log(m) + O(n)) time, O(m + n) time

        n = len(nums)
        trains = defaultdict(set)
        for i in range(n):
            if nums[i] == 0 or nums[i] == 1:
                continue
            num = nums[i]
            while primes[num] != num:
                trains[primes[num]].add(i)
                num //= primes[num]
            trains[primes[num]].add(i)
        visited_trains = set()
        min_jumps = [float("inf")] * n
        min_jumps[0] = 0
        queue = deque([0])
        adj_steps = (-1, 1)
        while queue:
            cur_station = queue.popleft()
            for step in adj_steps:
                if 0 <= cur_station + step < n and min_jumps[
                    cur_station + step
                ] == float("inf"):
                    min_jumps[cur_station + step] = min_jumps[cur_station] + 1
                    queue.append(cur_station + step)
            if (
                primes[nums[cur_station]] == nums[cur_station]
                and nums[cur_station] not in visited_trains
            ):
                visited_trains.add(nums[cur_station])
                for station in trains[nums[cur_station]]:
                    if min_jumps[station] == float("inf"):
                        min_jumps[station] = min_jumps[cur_station] + 1
                        queue.append(station)
        return min_jumps[n - 1]
