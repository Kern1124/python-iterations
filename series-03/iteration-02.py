from ib111 import week_10  # noqa
from typing import Dict, Set, Tuple, List, Optional

Heading = int
NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
Tile = Set[Heading]
Position = Tuple[int, int]
Plan = Dict[Position, Tile]

def navigate_rec(plan: Plan, start: Position, goal: Position,
                 visited: Set[Position], stack: List[Position]) -> bool:

    directions = {NORTH: (0, -1), SOUTH: (0, 1),
                  EAST: (1, 0), WEST: (-1, 0)}

    if start in visited:
        return False

    stack.append(start)
    visited.add(start)

    if start == goal:
        return True

    for direction in plan[start]:
        x, y = start

        x_shift, y_shift = directions[direction]
        move = x + x_shift, y + y_shift

        if navigate_rec(plan, move, goal, visited, stack):
            return True

    stack.pop()
    return False

def navigate(plan: Plan, start: Position, goal: Position) \
        -> Optional[List[Position]]:

    stack: List[Position] = []

    if navigate_rec(plan, start, goal, set(), stack):
        return stack

    return None

def main() -> None:
    plan = {(1, 1): {NORTH}, (1, 0): {SOUTH}, (2, 2): {EAST}, (3, 2): {WEST}}
    assert_correct_navigate(plan, (1, 1), (2, 2), False)
    assert_correct_navigate(plan, (1, 1), (1, 0), True)
    assert_correct_navigate(plan, (3, 2), (2, 2), True)

    plan = {
        (-2, -2): {EAST, SOUTH},
        (-1, -2): {EAST, WEST},
        (0, -2): {SOUTH, WEST},
        (-5, -1): {SOUTH},
        (-2, -1): {NORTH, SOUTH},
        (0, -1): {NORTH, SOUTH},
        (5, -1): {EAST, SOUTH},
        (6, -1): {SOUTH, WEST},
        (-5, 0): {NORTH, EAST, SOUTH},
        (-4, 0): {EAST, WEST},
        (-3, 0): {EAST, WEST},
        (-2, 0): {NORTH, EAST, WEST},
        (-1, 0): {EAST, WEST},
        (0, 0): {NORTH, EAST, SOUTH, WEST},
        (1, 0): {EAST, WEST},
        (2, 0): {EAST, SOUTH, WEST},
        (3, 0): {EAST, WEST},
        (4, 0): {EAST, WEST},
        (5, 0): {NORTH, EAST, WEST},
        (6, 0): {NORTH, WEST},
        (-5, 1): {NORTH},
        (0, 1): {NORTH, SOUTH},
        (2, 1): {NORTH, SOUTH},
        (-1, 2): {EAST},
        (0, 2): {NORTH, EAST, WEST},
        (1, 2): {EAST, WEST},
        (2, 2): {NORTH, WEST},
    }

    assert_correct_navigate(plan, (-5, -1), (-5, 1), True)
    assert_correct_navigate(plan, (-5, -1), (-1, 2), True)
    assert_correct_navigate(plan, (0, 0), (2, 2), True)

    plan[2, 0] = {WEST, SOUTH}
    plan[3, 0] = {EAST}

    assert_correct_navigate(plan, (3, 0), (6, -1), True)
    assert_correct_navigate(plan, (3, 0), (0, 0), False)
    assert_correct_navigate(plan, (-5, -1), (6, -1), False)

def assert_correct_navigate(plan: Plan, start: Position, goal: Position,
                            possible: bool) -> None:
    path = navigate(plan, start, goal)
    if possible:
        assert path is not None
        assert correct_path(plan, start, goal, path)
    else:
        assert path is None

def correct_path(plan: Plan, start: Position, goal: Position,
                 path: List[Position]) -> bool:
    if len(path) == 0 or path[0] != start or path[-1] != goal:
        return False

    dirs = {(0, -1): NORTH, (0, +1): SOUTH, (-1, 0): WEST, (+1, 0): EAST}

    lx, ly = path[0]
    for i in range(1, len(path)):
        x, y = path[i]
        if (x, y) not in plan:
            return False

        diff = x - lx, y - ly
        if dirs.get(diff) not in plan[lx, ly]:
            return False

        lx, ly = x, y

    return True

if __name__ == '__main__':
    main()
