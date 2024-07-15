class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        eightDChildren = 0
        money -= children
        eightDChildren = min(money // 7, children)
        money -= 7 * eightDChildren
        if money > 0:
            if eightDChildren == children and eightDChildren > 0:
                eightDChildren -= 1
            elif money == 3 and eightDChildren > 0 and children - eightDChildren == 1:
                eightDChildren -= 1
        return eightDChildren
