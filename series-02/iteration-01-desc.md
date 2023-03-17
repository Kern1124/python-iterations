#assignment-description

Imagine that we have a plan in the form of an unlimited square grid, on which square tiles with street or intersection sketches are placed (something like tiles in the game Carcassonne). We will represent these tiles as sets of directions in which the tile can be exited. For example, a tile ‹{NORTH, SOUTH}› is a street that runs north-south, a tile ‹{EAST, SOUTH, WEST}› is a T-shaped intersection, a tile ‹{EAST}› is a dead-end street (from that tile, it is only possible to move east, but nowhere else). We also allow an empty set, which is a tile that cannot be moved anywhere from.


We describe the situation on the square grid using a dictionary whose keys are coordinates and whose values are tiles. On coordinates that are not in the dictionary, there is no tile. Coordinates are in the format ‹(x, y)›, where ‹x› increases to the east and ‹y› increases to the south.

First, write a predicate ‹is_correct›, which returns ‹True› exactly when all the placed tiles are properly connected. That is, if it is possible to exit the tile in some direction, then there is another tile in that direction, and it is possible to return to this tile from that tile.

Next, implement a pure function ‹run›, which will simulate the movement of a robot on the plan and return its last position. Assume that the plan is correct (in the sense of the predicate ‹is_correct› above) and that the robot's initial position is on one of the placed tiles. The robot moves according to the following rules:

• At the initial position, the robot chooses the first direction in which it can move from the initial tile, in the order of north, east, south, west. If it is not possible to move from the initial position at all, the function ends.

• In the following steps, the robot prefers to stay in the original direction (i.e., if it can go straight, it will go straight). If this is not possible, the robot moves in another direction on the current tile – but it never returns in the direction it came from (if it reaches a dead-end street, it stops) and if it has more options, it chooses the one that means turning right for it.

• If the robot comes to a tile where it has been before, it stops.