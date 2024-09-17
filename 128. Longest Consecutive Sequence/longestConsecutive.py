class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n)
        nums_set = set(nums)
        max_len = 0
        for num in nums:
            if num - 1 not in nums_set:
                subseq_len = 1
                next_num = num + 1
                while next_num in nums_set:
                    subseq_len += 1
                    next_num += 1
                max_len = max(max_len, subseq_len)
        return max_len

        # O(nlog(n))
        # nums_set = sorted(set(nums))
        # max_len = 0
        # prev = None
        # for num in nums_set:
        #     if prev == num - 1:
        #         subseq_len += 1
        #     else:
        #         subseq_len = 1
        #     max_len = max(max_len, subseq_len)
        #     prev = num
        # return max_len
