import hilo.game.player as player
import hilo.game.card as card

def main():

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
        player1.change_points()
        #Change points method called
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
        




if __name__ == "__main__":
    main()