from copy import copy, deepcopy
class LittleGrid:
    def __init__(self, board):
        self.board = board
        self.starting_board = deepcopy(board)
    def get_row(self, row_number):
        return self.board[row_number]
    def get_column(self, column_number):
        return [self.board[0][column_number] , self.board[1][column_number],self.board[2][column_number]]
    def check_repeating(self):
        seen_numbers = []
        for r in self.board:
            for value in r:
                if value>=1 and value<=9 and not (value in seen_numbers):
                    seen_numbers.append(value)
                else:
                    return True
        return False
    def set_point(self,r, c, value):
        self.board[r%3][c%3] = value
    def get_point(self, r, c):
        return self.board[r%3][c%3]
    def get_starting_point(self, r, c):
        return self.starting_board[r%3][c%3]
    def reset(self):
        self.board = deepcopy(self.starting_board)
