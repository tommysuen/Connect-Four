from ps10pr4 import *

def main():
    while True:
        answer = input("Would you like to play Connect Four? Yes or No: ").lower()
        if answer == 'yes':
            PlayerMode = input("Single Player or Multi-Player? S or M: ").lower()
            if PlayerMode == 's':
                Player1 = 'X'
                print("You are X")
                connect_four(Player('X'), AIPlayer('O', 'RANDOM', 5))
                while True:
                    Redo = input("Play again? Y or N: ").lower()
                    if Redo == 'y':
                        connect_four(Player('X'), AIPlayer('O', 'RANDOM', 5))
                    elif Redo == 'n':
                       break
                        
            
            elif PlayerMode == 'm':
                Player1 = input("Player 1: Select X or O :").upper()
                if Player1 == 'X':
                    Player2 = 'O'
                    print("Player 2 is " + Player2)
                    connect_four(Player(Player1), Player(Player2))
                    while True:
                        Redo = input("Play again? Y or N: ").lower()
                        if Redo == 'y':
                            connect_four(Player(Player1), Player(Player2))
                        elif Redo == 'n':
                            break
            else:
                print("Invalid input. Please Try again")
                PlayerMode = input("Single Player or Multi-Player? S or M: ").lower()

        elif answer == 'no':
            return
        
if __name__== "__main__": main()
