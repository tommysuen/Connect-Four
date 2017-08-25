#
# ps10pr4.py (Problem Set 10, Problem 4)
#
# An AI Player for use in Connect Four
#

import random
from ps10pr3 import *

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """ put your docstring here
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)

        Player.__init__(self, checker)

        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def  __repr__(self):
        '''Returns the Player and their tiebreak and lookahead'''
        s = str(Player.__repr__(self))
        s += " (" + str(self.tiebreak) + ", " + str(self.lookahead) + ")"
        return s

    def max_score_column(self, scores):
        '''Finds the highest value in scores'''
        high = max(scores)
        lst = []
        for i in range(len(scores)):
            if scores[i] == high:
                lst += [i]
        if self.tiebreak == 'LEFT':
            return lst[0]
        elif self.tiebreak =='RIGHT':
            return lst[-1]
        elif self.tiebreak == 'RANDOM':
            return random.choice(lst)

    def scores_for(self, board):
        '''Finds the values for the player given the other player's best option'''
        scores = [0] * board.width
        for i in range(board.width):
            if board.slots[0][i] != " ":
                scores[i] = -1
            elif board.is_win_for(self.checker):
                scores[i] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[i] = 0
            elif self.lookahead == 0:
                scores[i] = 50
            else:
                board.add_checker(self.checker, i)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(board)
                scores[i] = 100 - max(opp_scores)
                board.remove_checker(i)
        return scores
    
    def next_move(self, board):
        '''Counts the number of moves and returns the highest value
           value of the scores'''
        self.num_moves += 1
        return self.max_score_column(self.scores_for(board))
        
        
                
