def createGrid(can, gridSize, canSize):
    can.bind("<Motion>", onMove)
    can.bind("<Button-1>", onClickLeft)
    can.bind("<Button-2>", onClickRight)
    can.bind("<Button-3>", onClickRight)

    cellSize = int(canSize / gridSize)

    can.create_line(0, 1, canSize, 1)
    can.create_line(1, 0, 1, canSize)
    can.create_line(canSize, 0, canSize, canSize)
    can.create_line(0, canSize, canSize + 1, canSize)

    for y in range(gridSize):
        can.create_line(y * cellSize, 0, y * cellSize, canSize)

    for x in range(gridSize):
        can.create_line(0, x * cellSize, canSize, x * cellSize)

def onMove(event):
    print ("x: ",event.x, "y:",event.y)

def onClickLeft(event):
    print ("Left:  x:",event.x, "y:",event.y)

def onClickRight(event):
    print ("Right: x:",event.x, "y:",event.y)

