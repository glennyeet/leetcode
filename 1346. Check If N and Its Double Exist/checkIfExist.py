from collections import Counter


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        for num in counter:
            if num == 0 and counter[num] >= 2:
                return True
            elif num != 0 and num * 2 in counter:
                return True
        return False
