

class Task:
    description: str
    remaining: int
    total: int

    def __init__(
            self,
            description: str = None,
            instances: int = 1,
            remaining: int = None
    ):
        self.description = description
        self.total = instances
        if remaining is None:
            self.remaining = instances
        else:
            self.remaining = remaining

    def __eq__(self, other):
        return self.description == other.description \
               and self.total == other.total \
               and self.remaining == other.remaining
