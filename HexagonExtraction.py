import math

import cv2
import numpy as np


def trimExcessArea(png, width, hy2, hy1, hx2, hx1):
    slope = (hy2 - hy1) / (hx2 - hx1)
    cy = hy2
    while cy > 0:
        cx = int((cy - hy1) / slope + hx1)
        cy = cy - 1
        if cx < width / 2:
            while cx >= 0:
                png[cy, cx] = [0, 0, 0, 0]
                cx = cx - 1
        else:
            while cx < width:
                png[cy, cx] = [0, 0, 0, 0]
                cx = cx + 1

def markHexagoninImg(image):
    write_clr = (255, 255, 255, 1)
    height, width, _ = image.shape
    side = height / math.sqrt(3)
    cord = math.sqrt(side * side - height / 2 * height / 2)
    hx1, hy1 = int((width - side) / 2), 0
    hx2, hy2 = int((width + side) / 2), 0
    hx3, hy3 = int((width + side) / 2 + cord), int(height / 2)
    hx4, hy4 = int((width + side) / 2), height
    hx5, hy5 = int((width - side) / 2), height
    hx6, hy6 = int((width - side) / 2 - cord), int(height / 2)
    pts = np.array([[hx1, hy1], [hx2, hy2], [hx3, hy3], [hx4, hy4], [hx5, hy5], [hx6, hy6]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    is_closed = True
    color = (255, 0, 0)
    thickness = 2
    image = cv2.polylines(image, [pts], is_closed, color, thickness)
    png = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    ht, wt, _ = png.shape
    side = height / math.sqrt(3)
    cord = math.sqrt(side * side - height / 2 * height / 2)
    cc = int((width - side) / 2 - cord)
    trimExcessArea(png, width, hy6, hy1, hx6, hx1)
    trimExcessArea(png, width, hy5, hy6, hx5, hx6)
    trimExcessArea(png, width, hy3, hy2, hx3, hx2)
    trimExcessArea(png, width, hy4, hy3, hx4, hx3)
    cv2.imwrite('HEAT_IMG/OUT/bgremoved.png', png)
    out = cv2.imread("HEAT_IMG/OUT/bgremoved.png", cv2.IMREAD_UNCHANGED)
    return out


def markHexagon():
    write_clr = (255, 255, 255, 255)
    path = 'HEAT_IMG/OUT/dimension.png'
    image = cv2.imread(path)
    height, width, _ = image.shape
    window_name = 'Image'
    side = height / math.sqrt(3)
    cord = math.sqrt(side * side - height / 2 * height / 2)
    hx1, hy1 = int((width - side) / 2), 0
    hx2, hy2 = int((width + side) / 2), 0
    hx3, hy3 = int((width + side) / 2 + cord), int(height / 2)
    hx4, hy4 = int((width + side) / 2), height
    hx5, hy5 = int((width - side) / 2), height
    hx6, hy6 = int((width - side) / 2 - cord), int(height / 2)
    pts = np.array([[hx1, hy1], [hx2, hy2], [hx3, hy3], [hx4, hy4], [hx5, hy5], [hx6, hy6]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    is_closed = True
    color = (255, 0, 0)
    thickness = 2
    image = cv2.polylines(image, [pts], is_closed, color, thickness)
    png = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    ht, wt, _ = png.shape
    side = height / math.sqrt(3)
    cord = math.sqrt(side * side - height / 2 * height / 2)
    cc = int((width - side) / 2 - cord)
    trimExcessArea(png, width, hy6, hy1, hx6, hx1)
    trimExcessArea(png, width, hy5, hy6, hx5, hx6)
    trimExcessArea(png, width, hy3, hy2, hx3, hx2)
    trimExcessArea(png, width, hy4, hy3, hx4, hx3)
    cv2.putText(png, "Side=" + str(int(side) / 100) + "m", (int(width * 2 / 5), 28), cv2.FONT_HERSHEY_DUPLEX, 0.8,
                write_clr, 2)
    cv2.imwrite('HEAT_IMG/OUT/bgremove.png', png)
    out = cv2.imread("HEAT_IMG/OUT/bgremove.png", cv2.IMREAD_UNCHANGED)
    cv2.imshow('out', out)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()


#markHexagon()
