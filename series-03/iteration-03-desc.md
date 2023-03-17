#assignment-description

The goal of this task is to write a pure function that solves verbal arithmetic puzzles, also known as cryptarithms or algebrograms, in a given positional system (which will always be an integer between 2 and 26, inclusive). A verbal arithmetic puzzle is a mathematical puzzle in which words are used instead of numerals in an equation, for example "SEND + MORE = MONEY". The objective is to assign each letter a unique digit, such that the equation holds true when the digits replace the letters. None of the numbers can begin with a zero. In the given example, the only possible solution (in decimal notation) is S → 9, E → 5, N → 6, D → 7, M → 1, O → 0, R → 8, Y → 2. After replacing the letters with digits, the equation holds true: ⟦9567 + 1085 = 10652⟧.

The function will take a string as input in the form of "word₁ + word₂ + ... + wordₙ = word", where there are at least two summands on the left side and exactly one word on the right side.

The function will return a dictionary that assigns a unique digit to each letter in the puzzle. If there are multiple solutions, the function can return any one of them. If there is no solution, the function will return None.

To solve the puzzle, the function should use backtracking. The approach is similar to carrying in long addition, where digits are assigned from right to left, one column at a time. Recursion should be terminated early when it becomes clear that a solution is impossible.