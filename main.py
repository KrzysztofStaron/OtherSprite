from tkinter import *
from grid import grid
from colorSelect import colorSelect

root = Tk()
root.title('OtherSprite')
root.resizable(False, False)
root.geometry("700x700")

canvasSize = 500
resolution = 8

#im = Image.new('RGB', (resolution, resolution))
#im.putdata([(255,0,0), (0,255,0), (0,0,255)])
#im.save('test.png')

canvasSize -= canvasSize % resolution
canvas = Canvas(root, width = canvasSize, height = canvasSize, bg = "white")
canvas.place(x = 100, y = 50)

newGrid = grid(canvas, resolution, canvasSize)

button = Button(root, text="save")

button.bind("<Button-1>", newGrid.saveFile)

button.place(x = 300, y = 560)

colors = Canvas(root, width = 200, height = 100, bg = "white")
newColorSelect = colorSelect(colors, 200, 100)
colors.place(x = 40, y = 560)

root.mainloop()