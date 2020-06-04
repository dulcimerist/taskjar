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

if __name__ == '__main__':
    unittest.main()