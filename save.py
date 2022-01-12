from PIL import Image
import math
from datetime import datetime

def save(colors):
    rgbColors = ["#ffffff"] * int(len(colors))

    for i in range(len(colors)):
        hex = colors[i].lstrip('#')
        rgbColors[i] = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

    size = int(math.sqrt(len(colors)))
    im = Image.new('RGB', (size, size))
    im.putdata(rgbColors)
    path = 'images/'+datetime.now().strftime("%d_%m_%Y")+'.png'
    open(path, "x")
    im.save(path)
    print("saved")
