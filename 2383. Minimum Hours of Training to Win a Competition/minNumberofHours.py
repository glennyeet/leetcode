class Solution:
    def minNumberOfHours(
        self,
        initialEnergy: int,
        initialExperience: int,
        energy: List[int],
        experience: List[int],
    ) -> int:
        totalEnergy = sum(energy)
        trainingHours = max(totalEnergy - initialEnergy + 1, 0)
        expAccumlated = initialExperience
        for exp in experience:
            if exp >= expAccumlated:
                trainingHours += exp - expAccumlated + 1
                expAccumlated += exp - expAccumlated + 1
            expAccumlated += exp
        return trainingHours
