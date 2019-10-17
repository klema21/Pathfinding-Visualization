import main
from tkinter import *

board = [ [0]*15 for _ in range(15) ]
start = (0, 0)
end = (0, 0)

counter = 0

root = Tk()
root.title("Pathfinding Visualization")
root.geometry("355x350")

def on_click(i, j, event):
    global counter
    global start
    global end
    if counter == 0:
        color = "red"
        start = (i, j)
    elif counter == 1:
        color = "green"
        end = (i, j)
    else:
        color = "black"
        board[i][j] = 1
    event.widget.config(bg=color)
    counter += 1


def run():
    result = main.main(board, start, end)
    del result[0]
    result.pop()
    for item in result:
        L = Label(root, text='    ', bg='yellow')
        L.grid(row=item[0]+1, column=item[1]+1)


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
