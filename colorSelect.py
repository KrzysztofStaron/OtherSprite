from tkinter import colorchooser
import json

class colorSelect():
    def __init__(self, can, canX, canY):
        with open('data.json') as json_file:
            data = json.load(json_file)
        self.color = (data["colorLeft"], data["colorRight"])

        self.can = can
        self.canX = canX
        self.canY = canY
        self.cellSize = round(self.canX / 2)

        self.can.bind("<Button-1>", self.onClickLeft)

        self.can.create_rectangle(0, 0, self.cellSize, self.canY, outline="#000", fill = self.color[0])
        self.can.create_rectangle(self.cellSize, 0, self.canX, self.canY, outline="#000", fill = self.color[1])

        self.fixEdges()

    def select(self):
        return colorchooser.askcolor()[1]

    def fixEdges(self):
        self.can.create_line(1, 1, self.canX, 1)
        self.can.create_line(1, 1, 1, self.canY)

    def onClickLeft(self, event):
        pos = event.x / self.cellSize
        pos -= pos % 1

        pos *= self.cellSize

        print(pos)
        selectedColor = self.select()
        print(selectedColor)
        if selectedColor == None:
            return ;
        self.can.create_rectangle(pos ,0 ,pos + self.cellSize ,self.cellSize , outline="#000", fill = selectedColor)

        with open('data.json') as json_file:
            data = json.load(json_file)
                        
            print(data)
            if pos / self.cellSize == 0:
                data["colorLeft"] = selectedColor
            else:
                data["colorRight"] = selectedColor


        with open('data.json', 'w') as f:
            json.dump(data, f)

        self.fixEdges()