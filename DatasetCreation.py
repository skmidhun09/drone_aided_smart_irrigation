import math

import cv2
from xlwt import Workbook

distance_ratio = 2.5
wb = Workbook()
row = 1
sheet1 = wb.add_sheet('Dataset')
sheet1.write(0, 0, 'x')
sheet1.write(0, 1, 'y')
sheet1.write(0, 2, 'angle')
sheet1.write(0, 3, 'flow_rate')
sheet1.write(0, 4, 'servo_angle')
sheet1.write(0, 5, 'distance')
count = 1

def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
    return ang + 360 if ang < 0 else ang


def excelwrite(x, y, angle, distance, flowrate, servoangle):
    global count
    sheet1.write(count, 0, x)
    sheet1.write(count, 1, y)
    sheet1.write(count, 2, angle)
    sheet1.write(count, 3, flowrate)
    sheet1.write(count, 4, servoangle)
    sheet1.write(count, 5, distance)
    count = count + 1


def processImage():
    print("sample height:")
    img = cv2.imread("Input/reference.png")
    height, width, _ = img.shape
    center_x = int(width / 2)
    center_y = int(height / 2)
    count = 1
    for y in range(1, height):
        for x in range(1, width):
            angle = int(getAngle((0, center_y), (center_x, center_y), (x, y)))
            distance = round((math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2) * distance_ratio) / 100, 2)
            if 2.65 > distance > 2.55:
                excelwrite(x, y, angle, distance, 5.8, 90)
            elif 2.45 > distance > 2.35:
                excelwrite(x, y, angle, distance, 5.67, 80)
            elif 2.25 > distance > 2.15:
                excelwrite(x, y, angle, distance, 5.53, 70)
            elif 1.90 > distance > 0.40:
                excelwrite(x, y, angle, distance, 4.46, int(0.26 * distance * 100))
            elif distance < 0.10:
                excelwrite(x, y, angle, distance, 1.1, int(0.26 * distance * 100))
    wb.save('Output\DataSet.xls')


processImage()
