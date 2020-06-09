from domain.Task import Task
from typing import List
from random import Random
from enum import Enum


class TaskBag:
    tasks: List[Task]
    escalateDraws: int
    cascadeDraws: int
    totalCascadeDraws: int
    shuffleDraws: int
    rng: Random

    def __init__(
            self,
            escalate_draws: int = 0,
            cascade_draws: int = 0,
            shuffle_draws: int = 0,
            tasks: List[Task] = [],
            rng: Random = Random()
    ):
        self.escalateDraws = escalate_draws
        self.cascadeDraws = cascade_draws
        self.totalCascadeDraws = cascade_draws
        self.shuffleDraws = shuffle_draws
        self.tasks = tasks
        self.rng = rng

    def shuffle(self):
        self.cascadeDraws = self.totalCascadeDraws
        for task in self.tasks:
            task.remaining = task.total

    def draw(self):
        sticks = self._get_sticks()

        if len(sticks) == 0:
            return TaskBagControl.RETRY

        nextIndex = self.rng.randint(0, len(sticks) - 1)
        if isinstance(sticks[nextIndex], TaskBagControl):
            return sticks[nextIndex]
        elif isinstance(sticks[nextIndex], Task):
            sticks[nextIndex].remaining -= 1
            return sticks[nextIndex].description

    def _get_sticks(self):
        returnValue = []
        for task in self.tasks:
            for i in range(task.remaining):
                returnValue.append(task)
        for i in range(self.escalateDraws):
            returnValue.append(TaskBagControl.ESCALATE)
        for i in range(self.cascadeDraws):
            returnValue.append(TaskBagControl.CASCADE)
        for i in range(self.shuffleDraws):
            returnValue.append(TaskBagControl.SHUFFLE)
        return returnValue


class TaskBagControl(Enum):
    ESCALATE = 0
    CASCADE = 1
    SHUFFLE = 2
    RETRY = 3
