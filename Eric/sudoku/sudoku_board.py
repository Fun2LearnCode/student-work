from little_grid import LittleGrid

class SudokuBoard:
    def __init__(self, board):
        self.sudoku_board = [[0 for x in range(3)] for y in range(3)]
        for r in range(3):
            for c in range(3):
                temp = [[0 for x in range(3)] for y in range(3)]
                for rr in range(3):
                    for cc in range(3):
                        temp[rr][cc] = board[rr + 3*r][cc+3*c]
                self.sudoku_board[r][c] = LittleGrid(temp)
    def check_board(self):
        seen_row = []
        seen_column = []
        for x in range(9):
            print(self.sudoku_board[int(x/3)][int(x/3)].check_repeating(), self.sudoku_board[int(x/3)][int(x/3)].board)
            if self.sudoku_board[int(x/3)][int(x/3)].check_repeating():
                return False

            for value in range(1,10):
                if value in self.get_row(x) and not value in seen_row:
                    seen_row.append(value)
                else:
                    return False
                if value in self.get_column(x) and not value in seen_column:
                    seen_column.append(value)
                else:
                    return False
            seen_row = []
            seen_column = []
        return True
    def get_row(self, row_number):
        temp =[]
        temp.extend(self.sudoku_board[int(row_number/3)][0].get_row(row_number%3))
        temp.extend(self.sudoku_board[int(row_number/3)][1].get_row(row_number%3))
        temp.extend(self.sudoku_board[int(row_number/3)][2].get_row(row_number%3))
        return temp
    def get_column(self, column_number):
        temp =[]
        temp.extend(self.sudoku_board[0][int(column_number/3)].get_column(column_number%3))
        temp.extend(self.sudoku_board[1][int(column_number/3)].get_column(column_number%3))
        temp.extend(self.sudoku_board[2][int(column_number/3)].get_column(column_number%3))
        return temp
    def get_point(self,x, y):
        return self.sudoku_board[int(x/3)][int(y/3)].get_point(x,y)
    def get_starting_point(self,x,y):
        return self.sudoku_board[int(x/3)][int(y/3)].get_starting_point(x,y)        
    def set_point(self,x,y, number):
        self.sudoku_board[int(x/3)][int(y/3)].set_point(x,y,number)

    def reset_board(self):
        for x in self.sudoku_board:
            for y in x:
                y.reset()
