import cv2
import numpy as np
def overlay_one():
    background = cv2.imread("overlay/rgb.png", cv2.IMREAD_UNCHANGED)
    foreground = cv2.imread("overlay/ir.png", cv2.IMREAD_UNCHANGED)
    # normalize alpha channels from 0-255 to 0-1
    alpha_background = 1
    alpha_foreground = 0.5
    # set adjusted colors
    for color in range(0, 3):
        background[:,:,color] = alpha_foreground * foreground[:,:,color] + \
            alpha_background * background[:,:,color] * (1 - alpha_foreground)
    # set adjusted alpha and denormalize back to 0-255
    background[:,:,3] = (1 - (1 - alpha_foreground) * (1 - alpha_background)) * 255
    # display the image
    cv2.imshow("Composited image", background)
    cv2.waitKey(0)

overlay_one()