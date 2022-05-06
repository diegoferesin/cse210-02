import random
class Card:
    number = 0
    """
    Individual cards are represented as a number from 1 to 13.

    Attributes:
        number (int): The value of the card
    """
    def set_number(self):
        self.number = random.randint(1,13)
    
    """
    This method will display the number obtained by the set_number method.
    """
    def display_number():
        pass