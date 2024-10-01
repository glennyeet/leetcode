from collections import Counter


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        arr_mod = []
        for num in arr:
            arr_mod.append(num % k)
        counter = Counter(arr_mod)
        for num in counter:
            second_num = (k - num) % k
            if (
                num == second_num
                and counter[num] % 2
                or counter[num] != counter[second_num]
            ):
                return False
        return True
