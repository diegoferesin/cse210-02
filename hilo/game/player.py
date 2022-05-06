from hilo.game.card import Card
class Player:
    """
        The player starts the game with 300 points
        and will draw cards and guess if the next card
        will be higher or lower than the previous; the 
        player will earn or lose points according to the
        accuracy of their guess.

        Attributes:
            points (int): keep track of the player's success in the game
    """
    def __init__(self):
        self.points = 300
        self.card = Card()
        '''
        Constructs a new instance of Player with a points and a card attribute.

        Args:
            self (Player): an instance of a Player
        '''

    def guess(self):
        higher_or_lower = input("Higher or lower? [h/l]")
        next_card = Card()
        print(f"Next card was: {next_card.get_number()}")
        if higher_or_lower == 'h':
            if next_card.get_number() > self.card.get_number():
                return True
            else:
                return False
        elif higher_or_lower == 'l':
            if next_card.get_number() < self.card.get_number():
                return True
            else:
                return False

    def guess():
        """Ask the player for the number to guess if is greater or lower.

        Args:
            self (Player): An instance of Player.
        """
        pass

    def change_points(self):
        """Updates the player's score.

        Args:
            self (Player): An instance of Player.
        """
        pass

    def play_again():
        """Asks the player to play again.

        Args:
            self (Player): An instance of Player.
        """
        pass
