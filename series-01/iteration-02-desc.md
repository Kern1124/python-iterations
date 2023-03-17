#assignment-description

In this homework, you will program a simplified version of the game "2048¹". Unlike the original game, we will only consider a one-dimensional game board, i.e. one row.

¹ ‹https://play2048.co/›

We will represent the game board using a list of non-negative integers, where zeros represent empty spaces. For example, the list ‹[2, 0, 0, 2, 4, 8, 0]› represents the following situation:

┌───┬───┬───┬───┬───┬───┬───┐
│ 2 │ │ │ 2 │ 4 │ 8 │ │
└───┴───┴───┴───┴───┴───┴───┘

The basic step of the game is to slide the row to the left or right. When sliding, all the numbers "fall" in the specified direction, and pairs of identical digits are summed up. Sliding the above list to the left results in ‹[4, 4, 8, 0, 0, 0, 0]›.

To try out the game (after solving the task), you have the file ‹game_2048.py› available, which you should place in the same directory as your solution file, or modify it according to the comments at the beginning and run it. The game is controlled by the left and right arrow keys, ‹R› resets the game, and ‹Q› quits.

Write a procedure ‹slide›, which performs a shift of the row represented by the list ‹row›, either to the left (if the parameter ‹to_left› has the value ‹True›) or to the right (if the parameter ‹to_left› has the value ‹False›). The procedure directly modifies the parameter ‹row› and returns ‹True› if there was any change due to the shift; otherwise, it returns ‹False›.