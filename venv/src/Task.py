from typing import List

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
    def getTask(self):
        return self.levels[0].tasks[0].description
    def getCollectionStatus(self):
        return self