from tkinter import *
import main

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.counter = 0
        #self.create_widget()
        #self.on_click()

        def create_widget(self):
            self.bttn = Button(self)
            self.bttn["Text"] = "Run"
            self.bttn["Command"] = self.run
            self.bttn.grid()

        def run(self):
            result = main.main(board)
            return result

        def on_click(self, i, j, event):
            global counter
            color = "red" if counter%2 else "black"
            event.widget.config(bg=color)
            board[i][j] = color
            board[i][j] = 1
            counter += 1

        for i, row in enumerate(self.board):
            for j, column in enumerate(row):
                L = Label(root, text='    ', bg="grey")
                L.grid(row=i+1, column=j+1)
                L.bind('<Button-1>', lambda e,i=i,j=j: on_click(i,j,e))


root = Tk()
root.title("Pathfinding Visualization")
root.geometry("300x300")
app = Application(root)
root.mainloop()
