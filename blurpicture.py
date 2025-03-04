#!/usr/bin/env python3

from images import Image
from functools import reduce

image = Image(input("Image path:\t"))

def blur(image):
    """Builds and returns a new image which is a
    blurred copy of the argument image."""
    def tripleSum(triple1, triple2):
        (r1, g1, b1) = triple1
        (r2, g2, b2) = triple2
        return (r1 + r2, g1 + g2, b1 + b2)
    new = image.clone()
    for y in range(1, image.getHeight() - 1):
        for x in range(1, image.getWidth() - 1):
            oldP = image.getPixel(x, y)
            left = image.getPixel(x - 1, y) # To left
            right = image.getPixel(x + 1, y) # To right
            top = image.getPixel(x, y - 1) # Above
            bottom = image.getPixel(x, y + 1) # Below
            sums = reduce(tripleSum, [oldP, left, right, top, bottom])
            averages = tuple(map(lambda x: x // 5, sums))
            new.setPixel(x, y, averages)
    new.draw()

blur(image)