from game.elements.cell import Cell


class World:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.board = [
            [Cell(0) for i in range(self.width)]
            for j in range(self.height)
        ]

    def get(self, x, y) -> int:
        return self.board[y][x].status

    def load(self, pattern: list, xo=0, yo=0):
        for y in range(len(pattern)):
            for x in range(len(pattern[y])):
                self.board[y+yo][x+xo] = Cell(pattern[y][x])

    def neighbors_coords(self, x, y):
        top = y - 1
        bottom = y + 1
        left = x - 1
        right = x + 1

        if top < 0:
            top = self.height - 1

        if bottom >= self.height:
            bottom = 0

        if left < 0:
            left = self.width - 1

        if right >= self.width:
            right = 0

        nb = [
            [left, top],    [x, top],       [right, top],
            [left, y],                        [right, y],
            [left, bottom], [x, bottom], [right, bottom]
        ]

        return nb

    def traverse(self):
        kills = []
        borns = []

        for y in range(self.height):
            for x in range(self.width):
                cell = self.board[y][x]
                cell.neighbors = 0
                neighbors = self.neighbors_coords(x, y)

                for i in neighbors:
                    xn, yn = i
                    neighbor = self.board[yn][xn]

                    if neighbor.alive():
                        cell.neighbors += 1

                if cell.alive():
                    if cell.neighbors < 2:
                        kills.append([x, y])
                    elif cell.neighbors > 3:
                        kills.append([x, y])

                else:
                    if cell.neighbors == 3:
                        borns.append([x, y])

        for coord in kills:
            x, y = coord
            self.board[y][x].kill()

        for coord in borns:
            x, y = coord
            self.board[y][x].born()

    def __iter__(self):
        return iter(self.board)
