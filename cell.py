class cell:
    def __init__(self, can):
        self.can = can
        self.obj = ""

    def setColor(self, color):
        self.can.itemconfig(self.obj, fill=color)