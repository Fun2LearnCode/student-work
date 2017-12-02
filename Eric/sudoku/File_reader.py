import json
import random
from sudoku_board import SudokuBoard
file = open("puzzels/eazy/one/compleete.json", "r")
json_parser = json.load(file)
class FileReader:
    def __init__(self):
        self.difficulty = "eazy"
        self.file = json.load(open("puzzels/"+self.difficulty+"/"+self.random()+"/incomplete.json", "r"))
        self.used_puzzles = []
        self.board = SudokuBoard(self.file)
        self.impossible = False
    def random(self):
        number = random.randint(0,3)
        if number == 1:
            return "one"
        elif number == 2:
            return "two"
        else:
            return "three"
    def load_newpuzzle(self):
        if self.impossible:
            print("loading new impossible")
            self.file = json.load(open("puzzels/"+self.difficulty+"/"+self.random()+"/compleete.json", "r"))
            self.board = SudokuBoard(self.file)
            x = random.randint(30, 81)
            while x>0:
                print("running forever in progress")
                r=random.randint(0,8)
                c=random.randint(0,8)
                if self.board.get_point(r,c) !=0:
                    self.board.set_point(r,c,0)
                    x=x-1
        else:
            self.file = json.load(open("puzzels/"+self.difficulty+"/"+self.random()+"/incomplete.json", "r"))
            self.board = SudokuBoard(self.file)
    def get_puzzle(self):
        return self.board
    def load_beginner(self):
        self.difficulty = "eazy"
        self.impossible = False
    def load_intermediate(self):
        self.difficulty = "meedium"
        self.impossible = False
    def load_advanced(self):
        self.difficulty = "harrrrrrrrrrrd"
        self.impossible = False
    def load_impossible(self):
        num = random.randint(0,3)
        if num ==1:
            self.difficulty = "eazy"
        elif num ==2:
            self.difficulty = "meedium"
        else:
            self.difficulty = "harrrrrrrrrrrd"
        self.impossible = True
