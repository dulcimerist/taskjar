from domain.Task import Task
from random import Random
from enum import Enum


class TaskBag:
    def __init__(
            self,
            escalate_draws: int = 0,
            total_cascade_draws: int = 0,
            remaining_cascade_draws: int = 0,
            shuffle_draws: int = 0,
            tasks=None,
            rng: Random = Random()
    ):
        if tasks is None:
            tasks = []
        self.escalateDraws = escalate_draws
        self.totalCascadeDraws = total_cascade_draws
        self.cascadeDraws = remaining_cascade_draws
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

    def __eq__(self, other):
        for task in self.tasks:
            if task not in other.tasks:
                return False

        return len(self.tasks) == len(other.tasks) \
            and self.escalateDraws == other.escalateDraws \
            and self.cascadeDraws == other.cascadeDraws \
            and self.totalCascadeDraws == other.totalCascadeDraws \
            and self.shuffleDraws == other.shuffleDraws


class TaskBagControl(Enum):
    ESCALATE = 0
    CASCADE = 1
    SHUFFLE = 2
    RETRY = 3
