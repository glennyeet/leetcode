class ProductOfNumbers:

    def __init__(self):
        self.prefix_products = []
        self.most_recent_zero_index = -1

    def add(self, num: int) -> None:
        # Prefix Sum: O(1) time, O(n) space

        if num == 0:
            self.prefix_products.append(1)
            self.most_recent_zero_index = len(self.prefix_products) - 1
        elif not self.prefix_products:
            self.prefix_products.append(num)
        else:
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        # Prefix Sum: O(1) time, O(1) space

        last_index = len(self.prefix_products) - k
        if last_index <= self.most_recent_zero_index:
            return 0
        elif last_index == 0:
            return self.prefix_products[-1]
        else:
            return self.prefix_products[-1] // self.prefix_products[last_index - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
