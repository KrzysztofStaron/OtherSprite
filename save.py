from PIL import ImageColor
from PIL import Image
import math


def save(colors):
    rgbColors = ["#ffffff"] * int(len(colors))

    for i in range(len(colors)):
        hex = colors[i].lstrip('#')
        print(hex)
        rgbColors[i] = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    
    size = int(math.sqrt(len(colors)))
    im = Image.new('RGB', (size, size))
    im.putdata(rgbColors)
    im.save('test.png')