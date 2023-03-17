from typing import Optional, Dict, Set

def solve_single(letters: str, result: Dict[str, int],
                 base: int, summed: int, no_zero: Set[str]) -> Optional[bool]:

    if len(letters) == 0 and summed == 0:
        return True

    elif len(letters) == 0:
        return None

    letter = letters[0]

    if letter == '=':
        r = result.get(letters[1])

        if r is not None:
            if r == summed % base and not (r == 0 and letters[1] in no_zero):
                return solve_single(letters[2:], result, base,
                                    0 + summed // base, no_zero)
            elif r != summed % base:
                return None

        else:
            if summed % base in result.values() or \
                   (summed % base == 0 and letters[1] in no_zero):
                return None
            else:
                result[letters[1]] = summed % base
                if solve_single(letters[2:], result, base,
                                0 + summed // base, no_zero):
                    return True

                result.pop(letters[1])
                return None

    if result.get(letter) is not None:
        summed += result[letter]
        letter = letters[0]

        if solve_single(letters[1:], result, base, summed, no_zero):
            return True
    else:

        for num in range(base):
            if num == 0 and letter in no_zero:
                continue

            if num in result.values():
                continue

            result[letter] = num

            if solve_single(letters[1:], result, base, summed + num, no_zero):
                return True

            result.pop(letter)

    return None


def solve(equation: str, base: int) -> Optional[Dict[str, int]]:

    result: Dict[str, int] = {}

    left_side = equation.split(" = ")[0].split(" + ")
    right_side = equation.split(" = ")[1]

    no_zero = set([word[0] for word in left_side]) | set([right_side[0]])
    equation = ""

    for i in range(len(right_side)):
        for word in left_side:

            if i < len(word):
                equation += (word[(-i - 1) % len(word)])

        equation += "=" + right_side[-i - 1]

    solve_single(equation, result, base, 0, no_zero)
    return result if result else None


def main() -> None:

    assert solve("SEND + MORE = MONEY", 10) \
        == {'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O': 0, 'R': 8, 'Y': 2}

    for base in range(2, 27):
        result = solve("XY + XY = YX", base)

        if base == 2 or base % 3 != 2:
            assert result is None
        else:
            x = base // 3
            y = 2 * x + 1
            assert result == {'X': x, 'Y': y}


if __name__ == '__main__':
    main()