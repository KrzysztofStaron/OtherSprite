from cell import cell

class grid():

    def __init__(self, can, gridSize, canSize):
        self.can = can
        self.gridSize = gridSize
        self.canSize = canSize
        self.cell = [[cell(self.can)] * gridSize] * gridSize
        self.cellSize = int(self.canSize / self.gridSize)

        self.can.bind("<Motion>", self.onMove)
        self.can.bind("<Button-1>", self.onClickLeft)
        self.can.bind("<Button-2>", self.onClickRight)
        self.can.bind("<Button-3>", self.onClickRight)
        self.createGrid()

    def createGrid(self):
        for x in range(self.gridSize):
            for y in range(self.gridSize):
                self.cell[x][y].obj = self.can.create_rectangle(x * self.cellSize, y * self.cellSize, x * self.cellSize + self.cellSize, y * self.cellSize + self.cellSize, outline="#000", fill="#fb0")

        self.can.create_line(0, 1, self.canSize, 1)
        self.can.create_line(1, 0, 1, self.canSize)
        self.can.create_line(self.canSize, 0, self.canSize, self.canSize)
        self.can.create_line(0, self.canSize, self.canSize + 1, self.canSize)

    def onMove(self, event):
        print ("x: ",event.x, "y:",event.y)

    def onClickLeft(self, event):
        print ("Left:  x:",event.x, "y:",event.y)

    def onClickRight(self, event):
        print ("Right: x:",event.x, "y:",event.y)

