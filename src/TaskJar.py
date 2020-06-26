import click

from domain.TaskBagCollection import TaskBagCollection
from helpers.FileIO import FileIO


@click.command()
@click.option("--file", default="./default", help="Filepath to file containing tasks")
def pick(file):
    tasks: TaskBagCollection = FileIO.parse(file)
    task: str = tasks.get_task()
    FileIO.save(file, tasks)
    print(task)


if __name__ == '__main__':
    pick()
