from typing import Optional, Dict, Set, Tuple

Heading = int
START, NORTH, EAST, SOUTH, WEST = -1, 0, 1, 2, 3
Tile = Set[Heading]

Position = Tuple[int, int]
Plan = Dict[Position, Tile]

def opposite_direction(direction: int) -> Optional[int]:
    reversed_directions = {NORTH: SOUTH, SOUTH: NORTH,
                           EAST: WEST, WEST: EAST}

    return reversed_directions.get(direction)

def next_pos(current_position: Position, direction: int) -> Position:
    x, y = current_position
    next_moves = {NORTH: (x, y - 1), SOUTH: (x, y + 1),
                  WEST: (x - 1, y), EAST: (x + 1, y)}

    return next_moves[direction]

def is_correct(plan: Plan) -> bool:
    for key in plan.keys():

        for direction in plan[key]:
            next_position = next_pos(key, direction)
            next_pos_directions = plan.get(next_position)

            if not next_pos_directions:
                return False

            if opposite_direction(direction) not in next_pos_directions:
                return False

    return True


def run(plan: Plan, start: Position) -> Position:
    visited = set()

    if not plan[start]:
        return start

    direction = min(plan[start])

    while start not in visited and plan[start]:

        visited.add(start)

        for next_direction in range(direction, direction + 4):
            next_direction = next_direction % 4

            if next_direction != opposite_direction(direction) \
                    and next_direction in plan[start]:
                direction = next_direction
                start = next_pos(start, direction)
                break

    return start

def main() -> None:
    assert is_correct({})
    assert is_correct({(1, 1): set()})
    assert is_correct({(1, 1): {NORTH}, (1, 0): {SOUTH}})
    assert is_correct({
        (3, 3): {NORTH, WEST},
        (2, 2): {SOUTH, EAST},
        (3, 2): {SOUTH, WEST},
        (2, 3): {NORTH, EAST},
    })

    assert not is_correct({(7, 7): {WEST}})
    assert not is_correct({(7, 7): {WEST}, (6, 7): set()})
    assert not is_correct({
        (3, 3): {NORTH, WEST},
        (2, 2): {SOUTH, EAST},
        (3, 2): {SOUTH, WEST},
        (2, 3): {NORTH},
    })

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

    assert run({(0, 0): set()}, (0, 0)) == (0, 0)
    assert run({(1, 1): {NORTH}, (1, 0): {SOUTH}}, (1, 1)) == (1, 0)
    assert run({(1, 1): {NORTH}, (1, 0): {SOUTH}}, (1, 0)) == (1, 1)

    assert is_correct(plan)

    assert run(plan, (0, 0)) == (-5, -1)
    assert run(plan, (-5, -1)) == (-5, 1)
    assert run(plan, (-4, 0)) == (5, 0)
    assert run(plan, (0, 1)) == (-5, -1)
    assert run(plan, (-1, 2)) == (5, 0)

    plan[2, 0] = {WEST, SOUTH}
    plan[3, 0] = {EAST}

    assert is_correct(plan)

    assert run(plan, (-4, 0)) == (-1, 2)
    assert run(plan, (1, 2)) == (-5, -1)

if __name__ == '__main__':
    main()
