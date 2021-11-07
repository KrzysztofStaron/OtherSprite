from tkinter import *
from grid import grid
from colorSelect import colorSelect


root = Tk()
root.title('OtherSprite')
root.resizable(False, False)
root.geometry("700x700")

canvasSize = 500
resolution = 8

canvasSize -= canvasSize % resolution
canvas = Canvas(root, width = canvasSize, height = canvasSize, bg = "white")
canvas.place(x = 100, y = 50)

newGrid = grid(canvas, resolution, canvasSize)

colors = Canvas(root, width = 200, height = 100, bg = "white")
newColorSelect = colorSelect(colors, 200, 100)
colors.place(x = 40, y = 560)

root.mainloop()