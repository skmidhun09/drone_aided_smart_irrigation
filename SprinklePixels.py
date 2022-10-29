import random
import time

import cv2

alpha = 1
pixelRatio = 5
deviationRandom = False


def deviation_sprinkle(img, y, x, deviation):
    if alpha > 0:
        for i in range(y - deviation, y + deviation + 1):
            for j in range(x - deviation, x + deviation + 1):
                if img[i, j].all() != img[y, x].all():
                    if deviationRandom:
                        if bool(random.getrandbits(1)):
                            img[i, j] = 200, 100, 0
                    else:
                        img[i, j] = 200, 100, 0


def sprinkle(img, y, x):
    img[y, x] = 200, 0, 0
    deviation = round(alpha * pixelRatio)
    deviation_sprinkle(img, y, x, deviation)
    cv2.imwrite('HEAT_IMG/OUT/watered.png', img)


def process_image():
    print("sample height:")
    img = cv2.imread("HEAT_IMG/OUT/heat20.png")
    height, width, _ = img.shape
    print(height, width)
    for y in range(1, height, pixelRatio):
        for x in range(1, width, pixelRatio):
            if pixelRatio > 1:
                for y1 in range(y, y + pixelRatio):
                    for x1 in range(x, x + pixelRatio):
                        if y1 < height and x1 < width:
                            (b, g, r) = img[y1, x1]
                            if b == 0 and g == 0 and r == 0:
                                sprinkle(img, y1, x1)
            else:
                (b, g, r) = img[y, x]
                if b == 0 and g == 0 and r == 0:
                    sprinkle(img, y, x)
            imgZoom = cv2.resize(img, (4 * width, 4 * height))
            cv2.imshow("Output", imgZoom)
            (b, g, r) = img[y, x]
            if b == 200:
                cv2.waitKey(20)


def find_area():
    img = cv2.imread("HEAT_IMG/OUT/watered.png")
    height, width, _ = img.shape
    count_a_dash = 0
    count_a = 0
    for y in range(1, height):
        for x in range(1, width):
            (b, g, r) = img[y, x]
            if b == 200 and g == 100:
                count_a_dash = count_a_dash + 1
            if b == 200 and g == 0:
                count_a = count_a + 1
    print("A dash:",count_a_dash, " Area: ",count_a)


process_image()
find_area()
