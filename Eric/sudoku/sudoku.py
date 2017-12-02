from tkinter import *
from tkinter import messagebox
import sudoku_board
from File_reader import FileReader
root = Tk()
file_reader = FileReader()
menu_bar = Menu(root)
game = Menu(root, tearoff = 0)
difficulty = Menu(root, tearoff = 0)
global global_x
global global_y
global_x = -1
global_y =-1

def display_puzzle(puzzle):
    for r in range(0,11):
        for c in range(0,11):
            display_board[r][c].delete("all")
    for r in range(0,9):
        print(file_reader.get_puzzle().get_row(r))
        for c in range(0,9):
            if puzzle.get_point(r,c) != 0:
                draw_number(c,r, puzzle.get_point(r,c))



def load_beginner():
    print("beginner")
    file_reader.load_beginner()
    file_reader.load_newpuzzle()
    board = file_reader.get_puzzle()
    display_puzzle(board)
def load_intermediate():
    print("Intermediate")
    file_reader.load_intermediate()
    file_reader.load_newpuzzle()
    board = file_reader.get_puzzle()
    display_puzzle(board)
def load_advanced():
    print("Advanced")
    file_reader.load_advanced()
    file_reader.load_newpuzzle()
    board = file_reader.get_puzzle()
    display_puzzle(board)
def load_impossible():
    print("Impossible?")
    file_reader.load_impossible()
    file_reader.load_newpuzzle()
    display_puzzle(file_reader.get_puzzle())

def reset_puzzle():
    file_reader.get_puzzle().reset_board()
    display_puzzle(file_reader.get_puzzle())

def new_puzzle():
    file_reader.load_newpuzzle()
    display_puzzle(file_reader.get_puzzle())

def check_puzzle():
    if file_reader.get_puzzle().check_board() == True:
        messagebox.showinfo("sudoku game", "You finished. You are smart")
    else:
        messagebox.showinfo("sudoku game", "Try again.")


display_board = [[0 for x in range(11)] for y in range(11)]

for x in range(11):
    for y in range(11):
        if (y==3 and not (x == 3 or x==7)) or  (y ==7 and not (x == 3 or x==7)):
            display_board[x][y]=Canvas(root, bg="black", height = 56, width = 3, bd=0, highlightthickness =0, relief = "ridge")
        elif (x==3 and not (y == 3 or y==7)) or (x ==7 and not (y == 3 or y==7)):
            display_board[x][y]=Canvas(root, bg="black", height = 3, width = 56, bd=0, highlightthickness =0, relief = "ridge")
        elif (x==3 or x == 7) and (y==3 or y==7):
            display_board[x][y]=Canvas(root, bg="black", height = 3, width = 3, bd=0, highlightthickness =0, relief = "ridge")
        else:
            display_board[x][y]=Canvas(root, bg="gray95", height = 50, width = 50, bd=3, highlightthickness =0, relief = "ridge")
        display_board[x][y].grid(row=x, column=y)

def click(event):
    global global_x
    global global_y
    x = root.winfo_pointerx() - root.winfo_rootx()
    y = root.winfo_pointery() - root.winfo_rooty()
    if x>168 and x<336:
        x+=-3
    elif x>336:
        x+=-6
    if y>168 and y<336:
        y+=-3
    elif y>336:
        y+=-6
    global_x = int(x/56)
    global_y = int(y/56)
def draw_number(x,y, number):
    if x>2 and x<6:
        x+=1
    elif x>=6:
        x+=2
    if y>2 and y<6:
        y+=1
    elif y>=6:
        y+=2
    display_board[y][x].delete("all")
    display_board[y][x].create_text(28,28,fill = "gray25", font = "Times 24 bold", text = number)
def display_number(event):
    if file_reader.get_puzzle().get_starting_point(global_y, global_x) ==0:
        file_reader.get_puzzle().set_point(global_y, global_x,int(event.char))
        draw_number(global_x, global_y, event.char)
    else:
        messagebox.showinfo("error", "You cannot change the board.")


difficulty.add_command(label = "Beginner", command = load_beginner)
difficulty.add_command(label = "Intermediate", command = load_intermediate)
difficulty.add_command(label = "Advanced", command = load_advanced)
difficulty.add_command(label = "Impossible?", command = load_impossible)

game.add_command(label = "Reset", command = reset_puzzle)
game.add_command(label="New puzzle", command = new_puzzle)
game.add_command(label="Check", command = check_puzzle)
menu_bar.add_cascade(label = "Game", menu = game)
menu_bar.add_cascade(label ="Difficulty", menu =difficulty)
root.config(menu = menu_bar)


root.bind("<Button-1>", click)
root.bind("1", display_number)
root.bind("2", display_number)
root.bind("3", display_number)
root.bind("4", display_number)
root.bind("5", display_number)
root.bind("6", display_number)
root.bind("7", display_number)
root.bind("8", display_number)
root.bind("9", display_number)






root.resizable(width= False, height =False)
root.mainloop()
