

class Board:
     """ a data type for a Connect Four board with
      arbitrary dimensions
     """
     def __init__(self, height, width):
         """ a constructor for Board objects """
         self.height = height
         self.width = width
         self.slots = [[' ']*width for r in range(height)]

     def __repr__(self):
        """ returns a string representation of a Board """
        s = '' # begin with an empty string
        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'
        s += '-' + '--' * self.width
        s += '\n'
        self.width2 = self.width
        output = 0
        while self.width2 > 0:
            self.width2 -= 1
            if output < 10:
                s += ' ' + str(output)
                output += 1
            else:
                output = output - 10
                s += ' ' + str(output)
                output += 1

        # add the row of hyphens to s
         # add the column indices to s
        return s
    
     def add_checker(self, checker, col):
        """ put your docstring here
       """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        # put the rest of the method here
        row = self.height -1
        while self.slots[row][col] != ' 'and row >= 0:
            row -= 1

        self.slots[row][col] = checker
        
     def reset(self):
        self.slots = [[' ']*self.width for r in range(self.height)]

     def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
        checkers in those columns of the called Board object, 
        starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'
                
     def can_add_to(self, col):
          for i in range(self.height):
              if self.slots[i][col] == ' ':
                  return True
          return False
     
     def is_full(self):
         for i in range(self.height):
             for t in range(self.width):
                 if Board.can_add_to(self, t) == True:
                     return False
         return True
        
     def remove_checker(self, col):
         for i in range(self.height):
             if self.slots[i][col] != ' ':
                 self.slots[i][col] = ' '
                 return
                
     def is_horizontal_win(self, checker):
         for row in range(self.height):
             for col in range(self.width-3):
                 if self.slots[row][col] == checker and \
                    self.slots[row][col + 1] == checker and \
                    self.slots[row][col + 2] == checker and \
                    self.slots[row][col + 3] == checker:
                    return True

         return False
        
     def is_vertical_win(self, checker):
         for row in range(self.height - 3):
             for col in range(self.width):
                 if self.slots[row][col] == checker and \
                    self.slots[row + 1][col] == checker and \
                    self.slots[row + 2][col] == checker and \
                    self.slots[row + 3][col] == checker:
                    return True

         return False

     def is_down_diagonal_win(self, checker):
         for row in range(self.height - 3):
             for col in range(self.width - 3):
                 if self.slots[row][col] == checker and \
                    self.slots[row + 1][col + 1] == checker and \
                    self.slots[row + 2][col + 2] == checker and \
                    self.slots[row + 3][col + 3] == checker:
                    return True

         return False

     def is_up_diagonal_win(self, checker):
         for row in range(3, self.height):
             for col in range(self.width - 3):
                 if self.slots[row][col] == checker and \
                    self.slots[row - 1][col + 1] == checker and \
                    self.slots[row - 2][col + 2] == checker and \
                    self.slots[row - 3][col + 3] == checker:
                    return True

         return False
     def is_win_for(self, checker):
        """ put your docstring here
         """
        assert(checker == 'X' or checker == 'O')

        # call the helper functions and use their return values to
        # determine whether to return True or False
        if Board.is_horizontal_win(self, checker) == True or \
           Board.is_vertical_win(self, checker) == True or \
           Board.is_down_diagonal_win(self, checker) == True or \
           Board.is_up_diagonal_win(self, checker) == True:
           return True
        return False
