from tkinter import *
from grid import grid
root = Tk()
root.title('OtherSprite')
root.resizable(False, False)
root.geometry("700x700")

canvasSize = 500
resolution = 16

canvasSize -= canvasSize % resolution
canvas = Canvas(root, width = canvasSize, height = canvasSize, bg = "white")
canvas.place(x = 100, y = 50)
newGrid = grid(canvas, resolution, canvasSize)

root.mainloop()