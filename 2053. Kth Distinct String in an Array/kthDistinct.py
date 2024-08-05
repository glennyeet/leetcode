class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = {}
        kth = 0
        for string in arr:
            counter[string] = counter.get(string, 0) + 1
        for key in counter.keys():
            if counter.get(key) == 1:
                kth += 1
            if kth == k:
                return key
        return ""
