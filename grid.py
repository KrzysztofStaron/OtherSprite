import json
from save import *

class grid():

    def __init__(self, can, gridSize, canSize):
        self.updateColors()

        self.can = can
        self.gridSize = gridSize
        self.canSize = canSize
        self.cell = ["#ffffff"] * gridSize * gridSize
        self.cellSize = int(self.canSize / self.gridSize)
        self.cellSize -= self.cellSize % 1

        self.can.bind("<Motion>", self.onMove)

        self.can.bind("<Button-1>", self.onClickLeft)
        self.can.bind("<Button-3>", self.onClickRight)
        self.createGrid()
        for x in range(10):
            print("\n")

    def updateColors(self):
        with open('data.json') as json_file:
            data = json.load(json_file)
        self.color = (data["colorLeft"], data["colorRight"])

    def createGrid(self):
        for x in range(self.gridSize):
            for y in range(self.gridSize):
                self.createCell(x, y)
        
        self.can.create_line(0, 1, self.canSize, 1)
        self.can.create_line(1, 0, 1, self.canSize)
        self.can.create_line(self.canSize, 0, self.canSize, self.canSize)
        self.can.create_line(0, self.canSize, self.canSize + 1, self.canSize)

    def onMove(self, event):
        pos = (event.x, event.y)

    def onClickLeft(self, event):
        self.updateColors()
        pos = self.mouseTocell(event.x, event.y)
        self.createCell(pos[0], pos[1], self.color[0])

    def onClickRight(self, event):
        self.updateColors()
        pos = self.mouseTocell(event.x, event.y)
        self.createCell(pos[0], pos[1], self.color[1])
    
    def mouseTocell(self, x, y):
        posX = x / self.cellSize
        posY = y / self.cellSize

        posX -= posX % 1
        posY -= posY % 1
        return int(posX), int(posY)

    def createCell(self, x, y, fillColor = "#ffffff"):
        self.cell[y * self.gridSize + x] = fillColor
        #print(self.cell[x])
        self.can.create_rectangle(x * self.cellSize, y * self.cellSize, x * self.cellSize + self.cellSize, y * self.cellSize + self.cellSize, outline="#000000", fill=fillColor)

        self.can.create_line(0, 1, self.canSize, 1)
        self.can.create_line(1, 0, 1, self.canSize)
        self.can.create_line(self.canSize, 0, self.canSize, self.canSize)
        self.can.create_line(0, self.canSize, self.canSize + 1, self.canSize)

    def saveFile(self, event):
        save(self.cell)