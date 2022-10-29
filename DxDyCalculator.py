import math

import numpy as np
import cv2
from xlwt import Workbook


def calculate():
    wb = Workbook()
    sheet1 = wb.add_sheet('Stabilization')
    sheet1.write(0, 0, 'Frame')
    sheet1.write(0, 1, 'left dy')
    sheet1.write(0, 2, 'right dy')
    sheet1.write(0, 3, 'top dx')
    sheet1.write(0, 4, 'bottom dx')
    sheet1.write(0, 5, 'dy')
    sheet1.write(0, 6, 'dx')
    sheet1.write(0, 7, 'da')
    cap = cv2.VideoCapture('Output/Stable.avi')
    w_frame, h_frame = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps, frames = cap.get(cv2.CAP_PROP_FPS), cap.get(cv2.CAP_PROP_FRAME_COUNT)
    x_left = int(1 * w_frame / 10)
    x_right = int(9 * w_frame / 10)
    y_top = 1 * int(h_frame / 10)
    y_bottom = 9 * int(h_frame / 10)
    frame_count = 1
    # print(w_frame,h_frame)
    while (cap.isOpened()):
        ret, frame = cap.read()
        # (r, g, b) = frame[119,119]
        # print(frame[0,0])
        # break
        if ret != True:
            break
        neg_left_dy = 0
        neg_right_dy = 0
        pos_left_dy = h_frame - 1
        pos_right_dy = h_frame - 1

        # frame[h,w]
        ############################# Vertical Data ##############################
        # left top corner -dy
        while (True):
            (r, g, b) = frame[neg_left_dy, x_left]
            if (int(r) + int(g) + int(b)) > 30:
                break
            if neg_left_dy > h_frame / 2:
                neg_left_dy = 0
                break
            neg_left_dy = neg_left_dy + 1
        # right top corner -dy
        while (True):
            (r, g, b) = frame[neg_right_dy, x_right]
            if (int(r) + int(g) + int(b)) > 30:
                break
            if neg_right_dy > h_frame / 2:
                neg_right_dy = 0
                break
            neg_right_dy = neg_right_dy + 1
        # left bottom corner +dy
        while (True):
            (r, g, b) = frame[pos_left_dy, x_left]
            if (int(r) + int(g) + int(b)) > 30:
                break
            if pos_left_dy < h_frame / 2:
                pos_left_dy = h_frame
                break
            pos_left_dy = pos_left_dy - 1
        # right bottom corner +dy
        while (True):
            (r, g, b) = frame[pos_right_dy, x_right]
            if (int(r) + int(g) + int(b)) > 30:
                break
            if pos_right_dy < h_frame / 2:
                pos_right_dy = h_frame
                break
            pos_right_dy = pos_right_dy - 1

        neg_top_dx = w_frame - 1
        neg_bottom_dx = w_frame - 1
        pos_top_dx = 0
        pos_bottom_dx = 0

        ############################# Horizontal Data ##############################
        # left top corner -dx
        while (True):
            (r, g, b) = frame[y_top, pos_top_dx]
            if (int(r) + int(g) + int(b)) > 30:
                break
            if pos_top_dx > w_frame / 2:
                pos_top_dx = 0
                break
            pos_top_dx = pos_top_dx + 1
        # right top corner -dx
        while (True):
            (r, g, b) = frame[y_bottom, pos_bottom_dx]
            if (int(r) + int(g) + int(b)) > 30:
                break
            if pos_bottom_dx > w_frame / 2:
                pos_bottom_dx = 0
                break
            pos_bottom_dx = pos_bottom_dx + 1
        # left bottom corner +dx
        while (True):
            (r, g, b) = frame[y_top, neg_top_dx]
            if (int(r) + int(g) + int(b)) > 30:
                break
            if neg_top_dx < w_frame / 2:
                neg_top_dx = w_frame
                break
            neg_top_dx = neg_top_dx - 1
        # right bottom corner +dx
        while (True):
            (r, g, b) = frame[y_bottom, neg_bottom_dx]
            if (int(r) + int(g) + int(b)) > 30:
                break
            if neg_bottom_dx < w_frame / 2:
                neg_bottom_dx = w_frame
                break
            neg_bottom_dx = neg_bottom_dx - 1
        sheet1.write(frame_count, 0, frame_count)
        left_dy = 0
        right_dy = 0
        if (neg_left_dy > 0):
            left_dy = 0 - neg_left_dy
        else:
            left_dy = h_frame - pos_left_dy - 1
        sheet1.write(frame_count, 1, left_dy)
        if (neg_right_dy > 0):
            right_dy = 0 - neg_right_dy
        else:
            right_dy = h_frame - pos_right_dy - 1
        sheet1.write(frame_count, 2, right_dy)

        top_dx = 0
        bottom_dx = 0
        if (pos_top_dx > 0):
            top_dx = pos_top_dx
        else:
            top_dx = 0 - (w_frame - neg_top_dx - 1)
        sheet1.write(frame_count, 3, top_dx)
        if (pos_bottom_dx > 0):
            bottom_dx = pos_bottom_dx
        else:
            bottom_dx = 0 - (w_frame - neg_bottom_dx - 1)
        sheet1.write(frame_count, 4, bottom_dx)

        ################# angle caculation from dx and dy)
        da = 0
        if left_dy > -1 and right_dy > -1:
            slope = (right_dy - left_dy) / (x_right - x_left)
            da = round(math.degrees(math.atan(slope)), 2)
        elif left_dy < 0 and right_dy < 0:
            slope = (abs(right_dy) - abs(left_dy)) / (x_right - x_left)
            da = round(math.degrees(math.atan(slope)), 2)
        else:
            slope = abs(right_dy) / (x_right - x_left)
            da = round(math.degrees(math.atan(slope)), 2)
        sheet1.write(frame_count, 5, round(((left_dy + right_dy) / 2), 0))
        sheet1.write(frame_count, 6, round(((top_dx + bottom_dx) / 2), 0))
        sheet1.write(frame_count, 7, da)

        print(frame_count)
        frame_count = frame_count + 1
    wb.save('Output\Stabilization.xls')


calculate()
