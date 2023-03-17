from typing import Dict, Tuple

Position = Tuple[int, int]


class Minesweeper:

    def __init__(self, width: int, height: int,
                 mines: Dict[Position, int]):
        self.width = width
        self.height = height
        self.score = 0
        self.status = [[' ' for _ in range(width)] for _ in range(height)]
        self.__mines = mines

    def get_radius(self, x: int, y: int) -> int:
        return self.__mines[(x, y)]

    def set_status(self, x: int, y: int, value: str) -> None:

        if x >= 0 and y >= 0 and x < self.width and y < self.height:

            if value >= '0' and value <= '8':
                self.score += 1

            if value == '*' and self.status[y][x] != '*':
                self.score -= 10

            if self.status[y][x] != '*':
                self.status[y][x] = value

    def is_mine(self, x: int, y: int) -> bool:

        if self.__mines.get((x, y)) is not None:
            return True

        return False

    def is_uncovered(self, x: int, y: int) -> bool:

        return self.status[y][x] != ' '

    def count_mines(self, x: int, y: int) -> int:

        count = 0

        for y_shift in [-1, 0, 1]:
            for x_shift in [-1, 0, 1]:

                if self.is_mine(x + x_shift, y + y_shift):
                    count += 1

        return count

    def flood_uncover(self, x: int, y: int) -> None:

        for y_shift in [-1, 0, 1]:
            for x_shift in [-1, 0, 1]:

                if y_shift == 0 and x_shift == 0:
                    continue

                self.uncover(x + x_shift, y + y_shift)

    def mine_explosion(self, x: int, y: int, radius: int) -> None:

        # This method could have been implemented with a modification of
        # uncover/flood_uncover, but I think it is better when it is written
        # as its own method.

        self.set_status(x, y, '*')

        for y_shift in range(-radius, radius + 1):
            for x_shift in range(-radius, radius + 1):

                if self.is_mine(x + x_shift, y + y_shift) and\
                       not self.is_uncovered(x + x_shift, y + y_shift):

                    shift_radius = self.get_radius(x + x_shift, y + y_shift)
                    self.mine_explosion(x + x_shift, y + y_shift, shift_radius)

                self.set_status(x + x_shift, y + y_shift, 'X')

    def uncover(self, x: int, y: int) -> None:

        if x >= 0 and y >= 0 and x < self.width and y < self.height:

            if not self.is_mine(x, y) and not self.is_uncovered(x, y):
                mine_count = self.count_mines(x, y)

                self.set_status(x, y, str(mine_count))

                if mine_count == 0:
                    self.flood_uncover(x, y)

            if self.is_mine(x, y):
                self.mine_explosion(x, y, self.get_radius(x, y))


def main() -> None:
    mines = {(2, 2): 5, (4, 5): 1, (6, 1): 0, (6, 3): 1, (6, 4): 3}

    ms = Minesweeper(8, 6, mines)
    assert ms.score == 0
    assert ms.status == [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]

    ms.uncover(1, 1)
    assert ms.score == 1
    assert ms.status == [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', '1', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]

    ms.uncover(0, 0)
    assert ms.score == 33
    assert ms.status == [
        ['0', '0', '0', '0', '0', '1', ' ', ' '],
        ['0', '1', '1', '1', '0', '1', ' ', ' '],
        ['0', '1', ' ', '1', '0', '2', ' ', ' '],
        ['0', '1', '1', '1', '0', '2', ' ', ' '],
        ['0', '0', '0', '1', '1', '3', ' ', ' '],
        ['0', '0', '0', '1', ' ', ' ', ' ', ' '],
    ]

    ms.uncover(5, 4)
    assert ms.score == 33
    assert ms.status == [
        ['0', '0', '0', '0', '0', '1', ' ', ' '],
        ['0', '1', '1', '1', '0', '1', ' ', ' '],
        ['0', '1', ' ', '1', '0', '2', ' ', ' '],
        ['0', '1', '1', '1', '0', '2', ' ', ' '],
        ['0', '0', '0', '1', '1', '3', ' ', ' '],
        ['0', '0', '0', '1', ' ', ' ', ' ', ' '],
    ]

    ms.uncover(4, 5)
    assert ms.score == 23
    assert ms.status == [
        ['0', '0', '0', '0', '0', '1', ' ', ' '],
        ['0', '1', '1', '1', '0', '1', ' ', ' '],
        ['0', '1', ' ', '1', '0', '2', ' ', ' '],
        ['0', '1', '1', '1', '0', '2', ' ', ' '],
        ['0', '0', '0', 'X', 'X', 'X', ' ', ' '],
        ['0', '0', '0', 'X', '*', 'X', ' ', ' '],
    ]

    ms.uncover(5, 5)
    assert ms.score == 23
    assert ms.status == [
        ['0', '0', '0', '0', '0', '1', ' ', ' '],
        ['0', '1', '1', '1', '0', '1', ' ', ' '],
        ['0', '1', ' ', '1', '0', '2', ' ', ' '],
        ['0', '1', '1', '1', '0', '2', ' ', ' '],
        ['0', '0', '0', 'X', 'X', 'X', ' ', ' '],
        ['0', '0', '0', 'X', '*', 'X', ' ', ' '],
    ]

    ms.uncover(6, 3)
    assert ms.score == -7
    assert ms.status == [
        ['0', '0', '0', '0', '0', '1', ' ', ' '],
        ['0', '1', '1', 'X', 'X', 'X', '*', 'X'],
        ['0', '1', ' ', 'X', 'X', 'X', 'X', 'X'],
        ['0', '1', '1', 'X', 'X', 'X', '*', 'X'],
        ['0', '0', '0', 'X', 'X', 'X', '*', 'X'],
        ['0', '0', '0', 'X', '*', 'X', 'X', 'X'],
    ]

    assert mines == {(2, 2): 5, (4, 5): 1, (6, 1): 0, (6, 3): 1, (6, 4): 3}


if __name__ == '__main__':
    main()