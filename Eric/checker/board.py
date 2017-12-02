from enums import Type
from piece import piece
global_x = -1
global_y = -1
from tkinter import *
root = Tk()

# Canvas(root, bg="red", height = 80, width = 80)
# grid(row =0, column=0)
# create_oval(5, 5, 75, 75, fill = "white")
# create_oval(10, 10, 70, 70, fill="red")

def compress(x,y):
    board[0][global_y][global_x].delete("all")
    board[1][y][x] = board[1][global_y][global_x]
    board[1][global_y][global_x] = 0
    create_piece( y,x)
def compress_jump(x,y,a,b):
    board[0][y+b][x+a].delete("all")
    board[0][global_y][global_x].delete("all")
    board[1][y][x] = board[1][global_y][global_x]
    board[1][global_y][global_x] = 0
    board[1][y+b][x+a] = 0
    create_piece( y,x)
def move(x,y):
    if board[1][global_y][global_x].type:
        if  abs(global_y - y)==1 and board[1][y][x] == 0 and abs(global_x - x) == 1:
            compress(x,y)
        # elif board[1][global_y][global_x].color == "black" and abs(global_y - y)==1 and board[1][y][x] == 0 and abs(global_x - x) == 1:
        #     compress(x,y)
    else:
        if board[1][global_y][global_x].color == "red" and global_y - y==1 and board[1][y][x] == 0 and abs(global_x - x) == 1:
            compress(x,y)
        elif board[1][global_y][global_x].color == "black" and global_y - y==-1 and board[1][y][x] == 0 and abs(global_x - x) == 1:
            compress(x,y)
def jump_piece(x,y):
    if board[1][global_y][global_x].type == False:
        if board[1][global_y][global_x].color == "black" and y> global_y:
            if x<global_x and board[1][y][x] ==0 and board[1][y-1][x+1].color=="red":#black left
                compress_jump(x,y,1,-1)
            elif x>global_x and board[1][y][x] ==0 and board[1][y-1][x-1].color=="red":#black right
                compress_jump(x,y,-1,-1)
        elif  board[1][global_y][global_x].color == "red" and y<global_y:
            if x<global_x and board[1][y][x] ==0 and board[1][y+1][x+1].color=="black":#red left
                compress_jump(x,y,1,1)
            elif x>global_x and board[1][y][x] ==0 and board[1][y+1][x-1].color=="black":#red right
                compress_jump(x,y,-1,1)
    elif board[1][global_y][global_x].type:
        if board[1][global_y][global_x].color == "black":
            if y<global_y:
                if x>global_x:
                    if board[1][y][x] ==0 and board[1][y+1][x-1].color=="red" :#black upper left
                        compress_jump(x,y,-1,1)
                elif x<global_x:
                    if board[1][y][x] ==0 and board[1][y+1][x+1].color=="red" :#black upper right
                        compress_jump(x,y,1,1)
            elif y> global_y:
                if x<global_x:
                    if board[1][y][x] ==0 and board[1][y-1][x+1].color=="red" :
                        compress_jump(x,y,1,-1)
                elif x>global_x:
                        compress_jump(x,y,-1,-1)
        elif board[1][global_y][global_x].color == "red":
            if y<global_y:
                if x> global_x:
                    if board[1][y][x] ==0 and board[1][y+1][x-1].color=="black" :
                        compress_jump(x,y, -1, 1)
                elif x<global_x:
                    if board[1][y][x] ==0 and board[1][y+1][x+1].color=="black" :
                        compress_jump(x,y,1,1)
            elif y>global_y:
                if x< global_x:
                    if board[1][y][x] ==0 and board[1][y-1][x+1].color=="black" :
                        compress_jump(x,y,1,-1)
                elif x > global_x:
                    if  board[1][y][x] ==0 and board[1][y-1][x-1].color=="black" :
                        compress_jump(x,y,-1,-1)
def create_piece(x, y):
    color = board[1][x][y].color
    board[0][x][y].create_oval(8, 8, 72, 72, fill = "white")
    board[0][x][y].create_oval(10, 10, 70, 70, fill=color)
    if board[1][x][y].type:
        board[0][x][y].create_oval(12, 12, 68, 68, fill = "white")
        board[0][x][y].create_oval(14, 14, 66, 66, fill=color)
def click(event):
    global global_x
    global turn
    global global_y
    x = int((root.winfo_pointerx() - root.winfo_rootx())/80)
    y = int((root.winfo_pointery() - root.winfo_rooty())/80)
    if board[0][y][x]["background"] == "black":
        if global_x == -1 :
            if board[1][y][x] != 0:
                if board[1][[y][x].color == "black":
                    global_x = x
                    global_y = y
                    board[0][y][x]["background"] = "blue"
                    turn+=1
                elif board[1][[y][x].color == "red":
                    global_x = x
                    global_y = y
                    board[0][y][x]["background"] = "blue"
                    turn+=1
        else:
            if board[1][y][x]!= 0 :
                board[0][global_y][global_x]["background"] = "black"
                board[0][y][x]["background"] = "blue"
                global_x = x
                global_y =y
            else:
                board[0][global_y][global_x]["background"] = "black"
                if abs(global_x-x) ==1 and abs(global_y-y)==1:
                    move(x,y)
                    turn+=1
                    if y==7 or y ==0:
                        board[1][y][x].type = True
                        create_piece( y,x)
                elif abs(global_x-x) ==2 and abs(global_y-y)==2:
                    jump_piece(x,y)
                    turn+=1
                    if y==7 or y ==0:
                        board[1][y][x].type = True
                        create_piece( y,x)
                global_x = -1
                global_y = -1
board = [[[0 for x in range(8)] for y in range(8)] for z in range(2)]
for x in range(8):
    for y in range(8):
        if x%2==0:
            if y%2==0:
                board[0][x][y]=Canvas(root, bg="red", height = 80, width = 80, bd=0, highlightthickness =0, relief = "ridge")
                board[0][x][y].grid(row=x, column=y)
            else:
                board[0][x][y]=Canvas(root, bg="black", height = 80, width = 80, bd=0, highlightthickness =0, relief = "ridge")
                board[0][x][y].grid(row=x, column=y)
                if x<=2:
                    board[1][x][y] = piece(Type.PAWN, Type.BLACK)
                    create_piece( x, y)
                elif x>=5:
                    board[1][x][y] = piece(Type.PAWN, Type.RED)
                    create_piece( x, y)
        else:
            if y%2 == 0:
                board[0][x][y]= Canvas(root, bg="black", height = 80, width = 80, bd=0, highlightthickness =0, relief = "ridge")
                board[0][x][y].grid(row=x, column=y)
                if x<=2:
                    board[1][x][y] = piece(Type.PAWN, Type.BLACK)
                    create_piece( x, y)
                elif x>=5:
                    board[1][x][y] = piece(Type.PAWN, Type.RED)
                    create_piece( x, y)
            else:
                board[0][x][y]= Canvas(root, bg="red", height = 80, width = 80, bd=0, highlightthickness =0, relief = "ridge")
                board[0][x][y].grid(row=x, column=y)



root.bind("<Button-1>", click)
root.resizable(width = False, height = False)
root.mainloop()
