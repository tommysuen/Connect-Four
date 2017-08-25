#
# ps10pr2.py (Problem Set 10, Problem 2)
#
# A Connect Four Player class 
#

from ps10pr1 import Board

# Write your class below.

class Player:
    
    def __init__(self, checker):
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        return "Player " + self.checker

    def opponent_checker(self):
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

    def next_move(self, board):
         self.num_moves += 1
         while True:
             col = int(input('Enter a column: '))
             b = board
             if col in range(b.width):
                 return col
             else:
                 print('Try Again!')
             
             
         
        
