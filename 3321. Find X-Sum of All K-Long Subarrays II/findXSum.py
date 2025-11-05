from typing import List
from collections import Counter
from sortedcontainers import SortedList


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        # Sliding Window + Hash Table + Ordered Set: O(n * log(n)) time, O(n) space

        n = len(nums)
        nums_counter = Counter()
        top_x_nums = SortedList()
        remaining_nums = SortedList()
        top_x_sum = 0

        def update_top_x_nums(num: int, delta: int) -> None:
            nonlocal top_x_sum
            if num in nums_counter:
                old_entry = (nums_counter[num], num)
                if old_entry in top_x_nums:
                    top_x_nums.remove(old_entry)
                    top_x_sum -= nums_counter[num] * num
                else:
                    remaining_nums.remove(old_entry)
            nums_counter[num] += delta
            if nums_counter[num] == 0:
                del nums_counter[num]
            else:
                remaining_nums.add((nums_counter[num], num))
            if remaining_nums and len(top_x_nums) < x:
                count, num = remaining_nums.pop()
                top_x_nums.add((count, num))
                top_x_sum += count * num
            elif top_x_nums and remaining_nums and remaining_nums[-1] > top_x_nums[0]:
                count_1, num_1 = top_x_nums.pop(0)
                count_2, num_2 = remaining_nums.pop()
                top_x_nums.add((count_2, num_2))
                remaining_nums.add((count_1, num_1))
                top_x_sum += count_2 * num_2 - count_1 * num_1

        for i in range(k):
            update_top_x_nums(nums[i], 1)
        answer = [top_x_sum]
        for i in range(k, n):
            update_top_x_nums(nums[i - k], -1)
            update_top_x_nums(nums[i], 1)
            answer.append(top_x_sum)
        return answer
