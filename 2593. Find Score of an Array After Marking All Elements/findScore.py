from heapq import heapify, heappop


class Solution:
    def findScore(self, nums: List[int]) -> int:
        p_queue = []
        for i, num in enumerate(nums):
            p_queue.append((num, i))
        heapify(p_queue)
        marked_nums = set()
        score = 0
        while p_queue:
            num, i = heappop(p_queue)
            score += num
            marked_nums.add((num, i))
            if i - 1 >= 0:
                marked_nums.add((nums[i - 1], i - 1))
            if i + 1 < len(nums):
                marked_nums.add((nums[i + 1], i + 1))
            while p_queue and p_queue[0] in marked_nums:
                heappop(p_queue)
        return score
