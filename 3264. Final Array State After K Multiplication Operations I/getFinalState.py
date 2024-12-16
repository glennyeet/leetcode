from heapq import heapify, heapreplace


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        p_queue = []
        for i, num in enumerate(nums):
            p_queue.append((num, i))
        heapify(p_queue)
        multiplied_nums = nums.copy()
        for _ in range(k):
            num, i = p_queue[0]
            new_num = num * multiplier
            heapreplace(p_queue, (new_num, i))
            multiplied_nums[i] = new_num
        return multiplied_nums
