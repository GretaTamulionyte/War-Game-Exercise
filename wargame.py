import random

class Card:
    suits  = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = {rank:value for value, rank in enumerate(
        ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"], start=2)}
        
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_rank_value(self):
        return self.ranks[self.rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = self.create_deck()
        random.shuffle(self.cards)


    def create_deck(self):
        return [Card(suit, rank) for suit in Card.suits\
        for rank in Card.ranks.keys()]

    def split_deck_in_two(self):
        computer_cards = []
        user_cards = []

        for i in range(len(self.cards)):
            if i % 2 == 0:
                computer_cards.append(self.cards[i])
            else:
                user_cards.append(self.cards[i])
        
        return computer_cards, user_cards



class Player:
    def __init__(self, name, cards):
        self.name = name
        self.hand = cards
    
    def draw_card(self):
        if self.hand:
            return self.hand.pop(0)
        else:
            return None

    def add_cards(self, cards):
        self.hand.extend(cards)

    def has_enough_cards(self, number):
        return len(self.hand) >= number

    
class GameSetup:
    def __init__(self):
        self.deck = Deck()
        computer_cards, user_cards = self.deck.split_deck_in_two()

        self.computer = Player("Computer", computer_cards)
        self.user = Player("User", user_cards)

    def get_players(self):
        return self.computer, self.user



class Game:
    def __init__(self):
        gamesetup = GameSetup()
        self.computer, self.user = gamesetup.get_players()
        self.round = Round(self.computer, self.user)

    def start_game(self):
        print("The game begins!\n\n\n")
        self.user_interaction()

    def user_interaction(self):
        while self.round.play_round():
            input("Press Enter to play the next round.\n\n\n")



class Round:
    def __init__(self, computer, user):
        self.computer = computer
        self.user = user
        # War is a special round, so a seperate class for it later on. self.war = War(computer, user)

    def play_round(self):
        input("Press Enter to draw a card\n\n\n")
        user_card = self.user.draw_card()
        computer_card = self.computer.draw_card()
        if not user_card or not computer_card:
            self.declare_winner(self.computer if not user_card else self.user)
            return False
        print(f"You play: {user_card}")
        print(f"Computer plays: {computer_card}\n\n\n")
        if user_card.get_rank_value() > computer_card.get_rank_value():
            self.user.add_cards([user_card, computer_card])
            print("You win the round and get to take the cards!\n\n\n")
        elif computer_card.get_rank_value() > user_card.get_rank_value():
            self.computer.add_cards([user_card, computer_card])
            print("Computer wins the round and gets to take the cards!\n\n\n")
        else:
            ...
            # Call the function play_war from class War, if one 
            # player doesn't have enough cards(will take care of this in class War), return False so as to close Game loop
            # if not self.war.play_war(cards here): return False 

        if not self.user.hand:
            self.declare_winner(self.computer)
            return False
        
        elif not self.computer.hand:
            self.declare_winner(self.user)
            return False

        return True

    def declare_winner(self, winner):
        print(f"{winner.name} wins! The opponent has no more cards!")


class War:
    def __init__(self, computer, user):
        self.computer = computer
        self.user = user

    def play_war(self, user_pile, computer_pile):
        print("This means WAR!")
        # In this version of the game, each player puts down 3 cards face down
        # and the fourth card face up. The last cards are the ones being compared.
        # If someone doesn't have enough cards for WAR, the winner is the one who has more
        # We'll Have to append to the player's pile all the cards put on the table, 
        # and access the last card(the fourth that is shown) to compare

        ...

    def declare_winner(self, winner):
        ...


if __name__ == "__main__":
    game = Game()
    game.start_game()



# Need to set up a counter for how many cards each player has after each round or WAR