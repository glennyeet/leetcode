class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fivesChange = tensChange = 0
        for bill in bills:
            if bill == 5:
                fivesChange += 1
            elif bill == 10:
                if fivesChange == 0:
                    return False
                fivesChange -= 1
                tensChange += 1
            else:
                if tensChange == 0 and fivesChange >= 3:
                    fivesChange -= 3
                elif tensChange > 0 and fivesChange > 0:
                    tensChange -= 1
                    fivesChange -= 1
                else:
                    return False
        return True
