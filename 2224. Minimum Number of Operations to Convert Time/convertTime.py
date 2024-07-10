class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        currentHour = int(current[0:2])
        currentMinutes = int(current[3:5])
        correctHour = int(correct[0:2])
        correctMinutes = int(correct[3:5])
        if correctMinutes >= currentMinutes:
            minutesLeft = correctMinutes - currentMinutes
            minOperations = correctHour - currentHour
        else:
            minutesLeft = 60 - currentMinutes + correctMinutes
            minOperations = correctHour - currentHour - 1
        minOperations += minutesLeft // 15
        minutesLeft -= minutesLeft // 15 * 15
        minOperations += minutesLeft // 5 + minutesLeft % 5
        return minOperations
