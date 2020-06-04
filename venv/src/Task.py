from typing import List
import random

class Task:
    description: str
    remaining: int = 1
    total: int = 1

class TaskLevel:
    tasks: List[Task] = []
    escalationChance: float = 0.0
    cascadeChance: float = 0.0
    shuffleChance: float = 0.0

class TaskCollection:
    levels: List[TaskLevel] = []

    @classmethod
    def withRNGSeed(cls, rngSeed):
        random.seed(rngSeed)
        return cls()

    def getTask(self):
        while True:
            nextIndex = random.randint(0, len(self.levels[0].tasks) - 1)
            if self.levels[0].tasks[nextIndex].remaining > 0:
                self.levels[0].tasks[nextIndex].remaining -= 1;
                return self.levels[0].tasks[nextIndex].description
    def getCollectionStatus(self):
        return self