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

    def change_points(self, score):
        """Updates the player's score according to the accuracy of their guess

        Args:
            self (Player): An instance of Player.
        """
        if score:
            points += 100
        else:
            points -= 75

    def display_points(self):
        print(f"Your score is: {self.points}")

    def display_card(self):
        print(f"The card is: {self.card.get_number}")
