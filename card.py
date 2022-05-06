import random
class Card:
    number = 0
    """
    Individual cards are represented as a number from 1 to 13.

    Attributes:
        number (int): The number of the different cards.
    """
    def set_number(self):
        self.number = random.randint(1,13)
    
    def display_number():
        pass