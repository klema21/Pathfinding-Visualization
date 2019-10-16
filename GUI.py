import main
from tkinter import *

board = [ [0]*10 for _ in range(10) ]

counter = 0

root = Tk()
root.title("Pathfinding Visualization")
root.geometry("300x300")

def on_click(i,j,event):
    global counter
    color = "red" if counter%2 else "black"
    event.widget.config(bg=color)
    #board[i][j] = color
    board[i][j] = 1
    counter += 1

def run():
    result = main.main(board)
    return result

for i,row in enumerate(board):
    for j,column in enumerate(row):
        L = Label(root,text='    ',bg='grey')
        L.grid(row=i+1,column=j+1)
        L.bind('<Button-1>',lambda e,i=i,j=j: on_click(i,j,e))

app = Frame(root)
app.grid()
bttn = Button(text="Run", command=run)
bttn.grid(row=0, column=0)
root.mainloop()
