from typing import List


class Task:
    description: str
    remaining: int
    total: int

    def __init__(
            self,
            description: str = None,
            instances: int = 1
    ):
        self.description = description
        self.total = instances
        self.remaining = instances
