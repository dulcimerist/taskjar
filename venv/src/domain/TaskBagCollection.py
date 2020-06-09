from typing import List
from random import Random
from domain.TaskBag import TaskBag, TaskBagControl


class TaskBagCollection:
    levels: List[TaskBag]
    _handlers = []

    def __init__(self, levels: List[TaskBag] = [], rng: Random = Random()):
        self.levels = levels
        for level in self.levels:
            level.rng = rng

    def get_task(self, level_index: int = 0) -> str:
        self._shuffle_if_no_tasks_remain()

        nextTask = self.levels[level_index].draw()

        if isinstance(nextTask, TaskBagControl):
            handler = self._get_handler(nextTask)
            return handler(level_index)
        else:
            return nextTask

    def get_tasks(self) -> List[TaskBag]:
        return self.levels

    def _get_handler(self, control: TaskBagControl):
        if control == TaskBagControl.ESCALATE:
            return self._escalate
        elif control == TaskBagControl.CASCADE:
            return self._cascade
        elif control == TaskBagControl.SHUFFLE:
            return self._shuffle
        elif control == TaskBagControl.RETRY:
            return self._retry


    def _escalate(self, level) -> str:
        return self.get_task(level + 1)

    def _cascade(self, level) -> str:
        self.levels[level].cascadeDraws -= 1
        return self.get_task(level - 1) + ',' + self.get_task(level - 1)

    def _shuffle(self, level) -> str:
        self._shuffle_all_bags()
        return self.get_task(level)

    def _retry(self, level) -> str:
        return self.get_task()

    def _shuffle_if_no_tasks_remain(self):
        for level in self.levels:
            for task in level.tasks:
                if task.remaining > 0:
                    return
        self._shuffle_all_bags()

    def _shuffle_all_bags(self):
        for level in self.levels:
            level.shuffle()
