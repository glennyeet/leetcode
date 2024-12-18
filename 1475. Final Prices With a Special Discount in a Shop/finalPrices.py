class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = prices.copy()
        stack = []
        for i, price in enumerate(prices):
            while stack and stack[-1][0] >= price:
                _, popped_i = stack.pop()
                answer[popped_i] -= price
            stack.append((price, i))
        return answer
