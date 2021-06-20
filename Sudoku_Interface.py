import Sudoku_Solver
from tkinter import *
import tkinter.messagebox


root = Tk()
root.title('Sudoku')
root.resizable(0, 0)
center = Frame(root, bg='blacks', width=900, height=900, padx=3, pady=3)
bottom = Frame(root, bg='white', width=50, height=50, padx=3, pady=3)


root.grid_rowconfigure(9, weight=1)
root.grid_columnconfigure(9, weight=1)
center.grid(row=0, sticky="nsew", padx=10, pady=10)
bottom.grid(row=9, sticky="nsew", padx=10, pady=10)


l = [[StringVar() for i in range(9)] for j in range(9)]

for row in range(9):
    for col in range(9):
        cell = Frame(center, bg='white', highlightbackground="black",
                     highlightcolor="black", highlightthickness=1,
                     width=50, height=50,  padx=20,  pady=13)
        cell.grid(row=row, column=col)

        l[row][col].set(Sudoku_Solver.sudoku_maze[row][col])
        Label(cell, textvariable=l[row][col], fg="black", font=("times new roman", 20, "bold")).pack()


def sol():

    if Sudoku_Solver.solveSudoku(Sudoku_Solver.sudoku_maze):
        for row in range(9):
            for column in range(9):
                l[row][column].set(Sudoku_Solver.sudoku_maze[row][column])
    else:
        tkinter.messagebox.showinfo("Wrong maze!", "No solution exists")


button = Button(bottom,text="Solve",width=10,bd=5,relief=GROOVE,font=("times new roman",13,"bold"), command=sol)
button.pack(side=RIGHT, padx=20)
mainloop()


