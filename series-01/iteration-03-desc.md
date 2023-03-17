#assignment-description

"FreeCell" is a solitaire card game that you may know as a part of certain company's operating systems based in Redmond. The game uses a classic deck of 52 cards with four suits and thirteen ranks from ace to king. The playing field contains:

free cells - typically four, in variants one to ten,
foundations - always exactly four, into each of which cards of the same suit are deposited, gradually from ace to king,
cascades - typically eight, in variants four to ten; all cards are dealt into the cascades at the beginning.
Allowed card moves are as follows:

cards can be moved from free cells and the bottom cards of cascades;
any card can be placed on an empty free cell or an empty cascade;
an ace of any suit can be placed on an empty foundation;
a card of the same suit with a value one higher can be placed on a card in a foundation;
another card can be placed on the bottom card of a cascade if its value is exactly one lower and its color is different (in the sense of red/black).
Cards are represented as pairs ‹(rank, suit)›, where rank is one of the numbers 1 to 13 (we have constants defined below for cards with values 1, 11, 12, 13) and suit is one of the numbers 0 to 3 (representing hearts, diamonds, clubs, and spades, respectively; also represented by constants below). Do not change the constants given here.

ACE, JACK, QUEEN, KING = 1, 11, 12, 13
HEARTS, DIAMONDS, CLUBS, SPADES = 0, 1, 2, 3
RED = -1
BLACK = -2

Implement the predicate ‹can_move›, i.e. whether it is possible to move a card in the given situation. The situation is represented by three lists, whose elements are either cards or ‹None›.

‹cascades› is a list of bottom cards of cascades (‹None› represents an empty cascade),
‹cells› is a list of cards in free cells (‹None› represents an empty cell),
‹foundation› is a list of top cards on foundations (‹None› represents an empty foundation).
Assume that the input situation is a real game situation (e.g. it is not possible for the same card to appear in two places).