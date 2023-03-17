def free_field(arena, field):

    player = (arena % 5 ** (field)) // 5 ** (field - 1)

    return arena - player * 5 ** (field - 1)


def find_player(arena, player):

    position = 0

    while arena != 0:

        current_player = arena % 5
        position += 1

        if current_player == player:
            return position

        arena //= 5

    return 0


def play(arena, player, throw):

    position = find_player(arena, player)

    arena = free_field(arena, throw + position)

    arena += player * 5 ** (throw + position - 1)

    if position != 0:
        arena -= player * (5 ** (position - 1))

    return arena


def main():

    for p in range(1, 5):
        assert play(0, p, 1) == p

    assert play(11, 3, 3) == 86
    assert play(84770, 4, 5) == 147250
    assert play(84770, 3, 4) == 240645
    assert play(12510, 1, 2) == 12505


if __name__ == '__main__':
    main()
