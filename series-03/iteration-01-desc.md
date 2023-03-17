#assignment-description

In this set, you will program one game, which will be "Minesweeper". Our version will be slightly modified, especially clicking on a mine will not necessarily mean the end of the game, but it will cause an explosion that damages part of the game board. (Each mine will have a "power" assigned to it, determining how many surrounding squares will be affected.)

To try the game (after implementing all the methods listed below), you have the file "game_minesweeper.py" available again, which you should run from the same directory as your solution file. At the beginning of the file, there are constants that you can adjust to change the size of the game board, the number of mines, and the appearance of the game.

The class "Minesweeper," which you have to implement, represents the state of the game, i.e., the content of the game board, the position of the mines, and the current score. The internal details are up to you. However, we expect objects of this class to have at least these two attributes:

• "status" - a 2D list (list of lists) representing the state of the game; elements of the inner lists are one-character strings:
◦ "' '" represents an unopened (and undamaged) square,
◦ "'*'" represents an exploded mine,
◦ "'X'" represents a square destroyed by an explosion,
◦ "'0'" to "'8'" represent an uncovered square with information about the number of neighboring mines.
• "score" - the number of points (an integer); points are awarded as follows:
◦ +1 point for each uncovered square without a mine,
◦ -10 points for each exploded mine.

Clicking on a square of the game board will be processed by the "uncover" method (see below). If the square is already uncovered or destroyed by an explosion, this method has no effect. Otherwise, the square is uncovered, and one of the following cases occurs:

• If there is a mine on this square, it explodes, and all squares within a distance less than or equal to the mine's power will be destroyed. If there was an unexploded mine on any of these squares, it will also explode. This can destroy more squares, and this process can be repeated (even multiple times). Squares where the mine exploded are marked with a state of "''" and other destroyed squares are marked with a state of "'X'" (the "''" state remains on the game board and does not change to "'X'" even after another explosion).
• Otherwise, the square state is set to "'0'" to "'8'" depending on the number of mines in the immediate vicinity. If the state is "'0'", all surrounding squares are uncovered, which can be repeated several times.

Here, the terms "vicinity" and "distance" are understood in all eight directions...