# War-Game-Exercise

Requirements for the program:

The task is to implement a children’s card game called War.
Read about it here: https://en.wikipedia.org/wiki/War_(card_game)
The main technical requirement is that you use the Object-Oriented Programming paradigm.




Implement a simple version of the Three Cards variation of the War Game

The variation: three cards are played face-down during a War, the fourth one is the one that is played face-up and compared with the other player's. If during a WAR a player doesn't have enough cards to engage in the WAR, the player who has more cards, wins.




Tasks, game rules, flow:

1. A standard 52-card deck needs to be initialized.
2. The deck of cards needs to be shuffled randomly.
3. Then it should be split evenly between two players.
4. Cards need to have a ranking so as to compare them.
5. Game consists of rounds and special rounds called WARS.
6. Round: both players (computer and user) need to play/show one card from the top of their deck. 
The player with the higher ranking card gets both cards and puts them to the back of his own personal deck (or "hand"). This concludes the round, another one begins.
7. EXCEPT if both players show cards of the same rank, then a special part of the game - WAR - begins.
8. WAR: both players need to take three cards from the top of their deck, put them face-down on the table. Then both players show the fourth card face-up.
The player who played the higher ranking card takes all the cards that were put down on the table (8 cards in total) and the WAR ends.
9. EXCEPT If both players show cards of the same rank, then another WAR commences.
10. See 8
11. When the WAR or WARS finally end, another normal round begins. And so on, and so on, till one player has all the cards, they are declared the winner and the game ends.




Additional considerations:

Separate classes for Card, Deck, Player, Game, Round, War...
Print what cards are being played by which player
Print who wins the round
Print how many cards each player has in their personal deck/ "hand" after each round or WAR
Print WAR! when a WAR begins
Print who wins the WAR
For convenience, the user should just press Enter to begin a round, to draw a card, etc.
Print who wins the whole game also
