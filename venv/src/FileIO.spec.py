import unittest
import os
from filecmp import cmp
from FileIO import FileIO
from domain.TaskBagCollection import TaskBagCollection
from domain.TaskBag import TaskBag
from domain.Task import Task

test_file_location = './temp.csv'
output_file_location = './actual.csv'
test_collection = TaskBagCollection([
    TaskBag(1, 0, 0, 0, [Task('Hello', 1), Task('World', 2)]),
    TaskBag(0, 1, 1, 1, [Task('Foo', 3, 0), Task('Bar', 4, 3)])
])


class TestFileIO(unittest.TestCase):

    def setUp(self) -> None:
        os.system('cp example_files/happypath.csv.backup %s' % test_file_location)

    def tearDown(self) -> None:
        os.system('rm %s' % test_file_location)
        # os.system('rm %s' % output_file_location)

    def test_parse(self):
        actual: TaskBagCollection = FileIO.parse(test_file_location)

        self.assertEqual(test_collection, actual)

    def test_save(self):

        FileIO.save(output_file_location, test_collection)

        self.assertTrue(cmp(test_file_location, output_file_location))

if __name__ == '__main__':
    unittest.main()
