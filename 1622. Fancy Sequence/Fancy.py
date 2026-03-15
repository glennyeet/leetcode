class Fancy:
    # Math: O(n) time, O(n) space for n operations

    def __init__(self):
        self.sequence = []
        self.mod_factor = 10**9 + 7
        self.multiplier = 1
        self.constant = 0

    def append(self, val: int) -> None:
        inverse_multiplier = pow(self.multiplier, self.mod_factor - 2, self.mod_factor)
        inverse_constant = -self.constant
        self.sequence.append(
            inverse_multiplier * (val + inverse_constant) % self.mod_factor
        )

    def addAll(self, inc: int) -> None:
        self.constant = (self.constant + inc) % self.mod_factor

    def multAll(self, m: int) -> None:
        self.multiplier = self.multiplier * m % self.mod_factor
        self.constant = self.constant * m % self.mod_factor

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.sequence):
            return -1
        return (self.sequence[idx] * self.multiplier + self.constant) % self.mod_factor


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
