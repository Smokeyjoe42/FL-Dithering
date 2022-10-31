from PIL import Image

#constants
PALLETSIZE = 1
div = 255//PALLETSIZE
pallet = []
curVal = 0

#creates the pallete
while curVal <= 255:
    pallet.append(curVal)
    curVal += div


def findNearestPalletColor(rgb):
    rgb = list(rgb)
    newRgb = [255, 255, 255]
    for j in range(3):
        low = 255
        for i in range(len(pallet)):
            curLow = abs(rgb[j] - pallet[i])
            if curLow < low:
                low = curLow
                newRgb[j] = pallet[i]
    return tuple(newRgb)

def f(error, rgb, factor):
    newRgb = [0,0,0]

    for i in range(3):
        newRgb[i] = int(rgb[i] + (error[i] * factor))
    return tuple(newRgb)

img = Image.open("uni.jpg")

for y in range(img.size[1]):
    print(y/img.size[1] * 100)
    for x in range (img.size[0]):
        oldPixel = list(img.getpixel((x,y)))
        newPixel = list(findNearestPalletColor(oldPixel))
        img.putpixel((x,y), tuple(newPixel))

        quantError = [ele1 - ele2 for(ele1, ele2) in zip(oldPixel, newPixel)]

        if x != img.size[0] -1:
            img.putpixel((x + 1, y), (f(quantError, img.getpixel((x + 1, y)), (7 / 16))))
        if x != 0 and y != img.size[1]-1:
            img.putpixel((x - 1, y + 1), (f(quantError, img.getpixel((x - 1, y + 1)), (3 / 16))))
        if y != img.size[1]-1:
            img.putpixel((x, y + 1), (f(quantError, img.getpixel((x, y + 1)), (5 / 16))))
        if x != img.size[0]-1 and y != img.size[1]-1:
            img.putpixel((x + 1, y + 1), (f(quantError, img.getpixel((x + 1, y + 1)), (1 / 16))))


img.show()
