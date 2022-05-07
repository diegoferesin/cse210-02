from hashlib import new
import hilo.game.player as player
import hilo.game.card as card

player1 = player.Player()
play="y"

"""
An intance of player is created.
The game is set to play
"""

while player1.points>0 and play.lower()=="y":
    """
    The game will continue as the player has > 0 points
    and decides to keep playing.
    """
    player1.display_card()
    #The current card is deplayed

    guess=input("Higher or lower? [h/l] ")

    new_card= card.Card()
    print(f"Next card was: {new_card}")
    """
    The new card is stores and displayed.
    """

    if guess.lower() == "h":
        if new_card > player1.card.get_number():
            player1.change_points(True)
        else:
            player1.change_points(False)
    elif guess.lower()=="l":
        if new_card > player1.card.get_number():
            player1.change_points(True)
        else:
            player1.change_points(False)

    """
    The new card is compared with the current card, if played guessed correctly point are added, if not substracted. If it has the same value, nothing happens.

    """        

    player1.card=new_card
    #The new card is now the Player's card.


    if player1.points <=0:
        player1.points=0
        play="n"
        print("You ran out of point to play.")
    """
    In order to be more visual appealing the score will not go under 0.
    """

    player1.display_points()   
    #points displayed.
    if player1.points!=0:             
        play=input("Play again? [y/n] ")

print("Thanks for playing!")
        