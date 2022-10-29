import cv2
import random
import math
from xlwt import Workbook

# Workbook is created

wb = Workbook()
sheet1 = wb.add_sheet('PatchDataSet')
sheet1.write(0, 0, 'No')
sheet1.write(0, 1, 'Radius')
sheet1.write(0, 2, 'Distance')
sheet1.write(0, 3, 'Angle')
sheet1.write(0, 4, 'Quadrant')


def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
    return ang + 360 if ang < 0 else ang


def processImage():
    print("sample height:")
    img = cv2.imread("Input/reference.png")
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width = gray_image.shape
    print(height, "sample", width)
    center_x = int(width / 2)
    center_y = int(height / 2)
    print("center reference", center_x, center_y)
    for n in range(1, 10001):
        x = random.randint(0, width-1)
        y = random.randint(0, height-1)
        print("circle center", x, y)
        if x < y:
            r = random.randint(1, int(height - y))
        else:
            r = random.randint(1, int(width - x))
        angle = int(getAngle((center_x, height), (center_x, center_y), (x, y)))
        p = [center_x, center_y]
        q = [x, y]
        dist = int(math.dist(p, q))
        print("Radius:", r)
        print("Distance:", dist)
        print("Angle: ", angle)
        quadrant = 0
        if angle < 90:
            quadrant = 1
        elif angle < 180:
            quadrant = 2
        elif angle < 270:
            quadrant = 3
        else:
            quadrant = 4
        sheet1.write(n, 0, n)
        sheet1.write(n, 1, r)
        sheet1.write(n, 2, dist)
        sheet1.write(n, 3, angle)
        sheet1.write(n, 4, quadrant)
        print(center_x, height, center_x, center_y, x, y)
    wb.save('Output\PatchDataSet.xls')


processImage()
