import csv

from domain.Task import Task
from domain.TaskBag import TaskBag
from domain.TaskBagCollection import TaskBagCollection


class FileIO:

    @staticmethod
    def parse(filepath: str) -> TaskBagCollection:
        returnValue: TaskBagCollection = TaskBagCollection()
        file = open(filepath)
        csv_reader = csv.reader(file, delimiter=',')

        next_line_control = True
        for row in csv_reader:
            if len(row) == 0:
                next_line_control = True
                continue

            if next_line_control:
                next_line_control = False
                returnValue.levels.append(TaskBag(
                    int(row[0]),
                    int(row[2]),
                    int(row[1]),
                    int(row[3])
                ))
            else:
                returnValue.levels[-1].tasks.append(Task(
                    row[2],
                    int(row[1]),
                    int(row[0])
                ))

        file.close()
        return returnValue

    @staticmethod
    def save(filepath: str, task_collection: TaskBagCollection):
        file = open(filepath, 'w')
        for bag in task_collection.levels:
            file.write("%s,%s,%s,%s\n" % (
              bag.escalateDraws,
              bag.cascadeDraws,
              bag.totalCascadeDraws,
              bag.shuffleDraws
            ))
            for task in bag.tasks:
                file.write("%s,%s,%s\n" % (
                    task.remaining,
                    task.total,
                    task.description
                ))
            if bag != task_collection.levels[-1]:
                file.write("\n")
        file.close()
