from player import Player
from card import Card

class Game:

    def __init__(self):

        self.isPlaying = True

        self.start_game()


    def start_game(self):

        player1 = Player()

        """
        An intance of player is created.
        The game is set to play
        """

        while self.isPlaying:
            """
            The game will continue as the player has > 0 points
            and decides to keep playing.
            """
            play(player1)
            end_game(player1)

                #The new card is now the Player's card.



        def play(player):
            player.display_card()
            #The current card is deplayed

            guess = input("Higher or lower? [h/l] ")
            if guess.lower() != "h" and guess.lower() != "l":
                print("Incorrect entry, please use 'h' or 'l'.")
            else:
                new_card = Card()
                print(f"Next card was: {new_card.get_number()}")
                """
                The new card is stores and displayed.
                """

                if guess.lower() == "h":
                    if new_card.get_number() > player.card.get_number():
                        change_points(player,True)
                    else:
                        change_points(player,False)
                elif guess.lower() == "l":
                    if new_card.get_number() < player.card.get_number():
                        change_points(player,True)
                    else:
                        change_points(player,False)

                """
                The new card is compared with the current card, if played guessed correctly point are added, if not substracted. If it has the same value, nothing happens.

                """        

                player.card = new_card
            

        def change_points(player, guess):
            """Updates the player's score according to the accuracy of their guess

            Args:
                self (Player): An instance of Player.
            """
            if guess==True:
                player.points+=100
            elif guess==False:
                player.points-=75

        def end_game(self, player):
            if player.points <= 0:
                player.points = 0
                self.isPlaying=False
                print("You ran out of point to play.")

                """
                In order to be more visual appealing the score will not go under 0.
                """

                player.display_points()   
                #points displayed.
            if player.points != 0:
                while True:  
                    play = input("Play again? [y/n] ")
                    if play.lower() != "y" and play.lower() != "n":
                        print("Incorrect entry, please use 'y' or 'n'.")
                    else:
                        if play.lower() == "y":
                            self.isPlaying=True
                        elif play.lower() == "n":
                            self.isPlaying=False
                        break

            print("Thanks for playing!")


            