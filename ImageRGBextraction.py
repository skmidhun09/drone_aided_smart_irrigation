import cv2
import numpy as np


image = cv2.imread("HEAT_IMG/OUT/rgb.png")
count = 0
height, width, _ = image.shape
x, y, h, w = 0, 0, height, width
red_channel = image
red_channel[:, :, 1] = 0
red_channel[:, :, 2] = 0
red_img = np.zeros(image.shape)
red_img = red_channel
for y in range(0, height):
    for x in range(0, width):
        b,g,r = red_img[y, x]
        if r <= 80:
            count += 1
            #red_img[y, x] = 0
cv2.imwrite('HEAT_IMG/OUT/Area.png',red_img)
cv2.imshow("Output", image)
cv2.waitKey(0)
# cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file

