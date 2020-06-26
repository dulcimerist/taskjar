import unittest
from random import Random
from domain.Task import Task
from domain.TaskBag import TaskBag
from domain.TaskBagCollection import TaskBagCollection


class TestTaskBagCollection(unittest.TestCase):
    def test_getTask_oneLevel_oneTask(self):
        subject = TaskBagCollection([
            TaskBag(0, 0, 0, 0, [
                Task("1")
            ])
        ])

        self.assertEqual("1", subject.get_task())

    def test_getTask_oneLevel_manyTasks(self):
        subject = TaskBagCollection([
            TaskBag(0, 0, 0, 0, [
                Task("2a"),
                Task("2b")
            ])
        ], Random(1))

        self.assertEqual("2a", subject.get_task())
        self.assertEqual("2b", subject.get_task())

    def test_getTask_manyLevels_manyTasks(self):
        subject = TaskBagCollection([
            TaskBag(2, 0, 0, 0, [
                Task("3a"),
                Task("3b")
            ]),
            TaskBag(0, 0, 0, 0, [
                Task("3c"),
                Task("3d")
            ])
        ], Random(3))

        self.assertEqual("3b", subject.get_task())
        self.assertEqual("3c", subject.get_task())
        self.assertEqual("3d", subject.get_task())
        self.assertEqual("3a", subject.get_task())

    def test_getTask_multipleDraws(self):
        subject = TaskBagCollection([
            TaskBag(0, 0, 0, 0, [
                Task("4a", 2)
            ])
        ])

        self.assertEqual("4a", subject.get_task())
        self.assertEqual("4a", subject.get_task())

    def test_getTask_noDrawsRemaining(self):
        # Should reset the remaining amount on each task before drawing another one

        subject = TaskBagCollection([
            TaskBag(1, 0, 0, 0, [
                Task("5a", 2)
            ]),
            TaskBag(0, 0, 0, 0, [
                Task("5b")
            ])
        ], Random(1))

        self.assertEqual("5a", subject.get_task())
        self.assertEqual("5a", subject.get_task())
        self.assertEqual("5b", subject.get_task())
        self.assertEqual("5a", subject.get_task())

    def test_getTask_cascade(self):
        subject = TaskBagCollection([
            TaskBag(1, 0, 0, 0, []),
            TaskBag(1, 0, 0, 0, [
                Task("6a"),
                Task("6b")
            ]),
            TaskBag(0, 1, 1, 0, [])
        ], Random(1))

        self.assertEqual("6b,6a", subject.get_task())

    def test_getTask_shuffle(self):
        subject = TaskBagCollection([
            TaskBag(0, 0, 0, 1,[
                Task("6a", 3)
            ])
        ], Random(1))

        subject.get_task()
        subject.get_task()

        remainingTasks = 0
        for level in subject.get_tasks():
            for task in level.tasks:
                remainingTasks += task.remaining
        self.assertEqual(2, remainingTasks)


if __name__ == '__main__':
    unittest.main()
