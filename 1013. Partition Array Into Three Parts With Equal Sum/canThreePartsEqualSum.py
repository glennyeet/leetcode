class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        arrSum = sum(arr)
        if arrSum % 3 != 0:
            return False
        partSum = arrSum // 3
        parts = 0
        counter = 0
        for i in range(len(arr)):
            counter += arr[i]
            if counter == partSum:
                parts += 1
                counter = 0
        if parts < 3:
            return False
        return True
