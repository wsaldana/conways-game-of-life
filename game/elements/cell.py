class Cell:
    def __init__(self, status: int) -> None:
        self.status = status
        self.neighbors = 0

    def kill(self):
        self.status = 0
        self.neighbors = 0

    def born(self):
        self.status = 1

    def alive(self) -> int:
        return bool(self.status)

    def __str__(self) -> str:
        return str(self.status)
