from PIL import Image
import numpy as np
import sys
import random

img = Image.open("start.png").convert("RGB")
img_array = np.array(img)

endimg = Image.open("end.png").convert("RGB")


attacking_color = eval(sys.argv[1])

Y, X = np.asarray(np.all(img_array==list(attacking_color), axis=2)).nonzero()

startingpixels = list(zip(X, Y))
print(startingpixels)

pixelmap = img.load()
endmap = endimg.load()

visited = {}

def test(pixelmap, endmap, coords, startingpixels, attacking_color, visited):
    if (coords in visited):
        return
    elif (pixelmap[coords] != attacking_color and endmap[coords] == attacking_color):
        startingpixels.append(coords)
        visited[coords] = True
        print(coords)

count = 1
while len(startingpixels) != 0:
    curpixels = startingpixels.copy()
    startingpixels = []
    for pixel in curpixels:
        pixelmap[pixel] = attacking_color
        if random.random() < 0.5:
            test(pixelmap, endmap, (pixel[0], pixel[1]+1), startingpixels, attacking_color, visited)
            test(pixelmap, endmap, (pixel[0], pixel[1]-1), startingpixels, attacking_color, visited)
            test(pixelmap, endmap, (pixel[0]+1, pixel[1]), startingpixels, attacking_color, visited)
            test(pixelmap, endmap, (pixel[0]-1, pixel[1]), startingpixels, attacking_color, visited)
        else:
            startingpixels.append(pixel)
    img.save(f"output{count}.png")
    count+=1


print('Attacking color: ', attacking_color)


