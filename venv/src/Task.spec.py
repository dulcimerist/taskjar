import unittest
from Task import Task
from Task import TaskLevel
from Task import TaskCollection
from typing import List

class TestTasks(unittest.TestCase):
    def test_getTask_oneLevel_oneTask(self):
        testTask = Task()
        testTask.description = "test123"

        testLevel = TaskLevel()
        testLevel.tasks.append(testTask)

        tasks = TaskCollection()
        tasks.levels.append(testLevel)

        self.assertEqual("test123", tasks.getTask())

    def test_getTask_oneLevel_manyTasks(self):
        testTask1 = Task()
        testTask1.description = "test123"
        testTask2 = Task()
        testTask2.description = "foobar"
        testLevel = TaskLevel()
        testLevel.tasks.append(testTask1)
        testLevel.tasks.append(testTask2)
        tasks = TaskCollection.withRNGSeed(1)
        tasks.levels.append(testLevel)

        actual = [tasks.getTask(), tasks.getTask()]

        self.assertEqual(testTask1.description, actual[0])
        self.assertEqual(testTask2.description, actual[1])

if __name__ == '__main__':
    unittest.main()