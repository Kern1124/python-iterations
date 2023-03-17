#assignment-description

Let's consider a game with four players and the following rules:

• The game board is one-dimensional, with unlimited length and a marked starting square;
• Each player has one playing piece, initially placed on the starting square;
• Players take turns rolling a die and moving their playing piece the number of spaces indicated by the roll;
• If a player's playing piece would land on a square already occupied by another player's playing piece, that piece is "kicked out" (as in the game "Sorry!") and returned to the starting square.

We will represent the situation on the game board using a non-negative integer, where its representation in base 5 represents the occupancy of individual squares excluding the starting square. The digit 0 represents an empty square, while the digits 1-4 represent occupancy by a specific player's piece. The movement of the pieces in the base 5 representation occurs from "right to left", i.e. from lower to higher orders.

