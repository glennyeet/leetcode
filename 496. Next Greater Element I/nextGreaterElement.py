class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greatest = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                next_greatest[stack.pop()] = num
            stack.append(num)
        ans = []
        for num in nums1:
            if num not in next_greatest:
                ans.append(-1)
            else:
                ans.append(next_greatest[num])
        return ans
