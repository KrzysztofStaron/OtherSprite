from tkinter import *
import grid

root = Tk()
root.attributes('-fullscreen', False)
root.geometry("700x700")

canvasSize = 500

canvas = Canvas(root, width = canvasSize, height = canvasSize, bg = "white")
canvas.place(x = 100, y = 100)

grid.createGrid(canvas, 10, canvasSize)

root.mainloop()