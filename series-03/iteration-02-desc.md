#assignment-description

Let's return to the robot whose movement we simulated in the second set of tasks (‹c_robot›). We will have the same plan again in the form of an unlimited square grid with square tiles depicting streets or intersections. However, this time we will give the robot the ability to move in any direction according to the possibilities on the current tile.

Implement the pure function ‹navigate›, which will return the path that the robot will take from the specified starting position to the specified target position on the specified grid. If no such path exists, the function will return ‹None›. The returned path is in the form of a list of all positions that the robot will pass through from the starting to the target position, inclusive. Assume that the plan is correct, i.e., it satisfies the predicate ‹is_correct› from task ‹s2/c_robot›, and that the specified positions are on one of the placed tiles.

Recommendation: Use the principle of backtracking. You will have to arrange something so that the robot does not run in circles (otherwise, your function may not terminate).