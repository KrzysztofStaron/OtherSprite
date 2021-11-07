from tkinter import *
from grid import grid
root = Tk()
root.title('OtherSprite')
root.geometry("700x700")

canvasSize = 500

canvas = Canvas(root, width = canvasSize, height = canvasSize, bg = "white")
canvas.place(x = 100, y = 100)
newGrid = grid(canvas, 10, canvasSize)
newGrid.createGrid()

root.mainloop()