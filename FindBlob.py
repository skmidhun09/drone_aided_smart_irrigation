# Standard imports
import math

import cv2
import numpy as np

import GPSCoordinates
import HexagonExtraction

single_pxl_area = 0.76
lat = 36.8487628
long = -76.2653029
# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()
# Change thresholds
params.minThreshold = 1
# Filter by Area.
params.filterByArea = True
params.minArea = 2000
params.maxArea = 100000
# Filter by Circularity
params.filterByCircularity = False
params.minCircularity = 0.1
# Filter by Convexity
params.filterByConvexity = False
params.minConvexity = 0.8
# Filter by Inertia
params.filterByInertia = False
params.minInertiaRatio = 0.01

# Read image
img = cv2.imread("HEAT_IMG/OUT/diskheat1.png")
color_img = cv2.imread("HEAT_IMG/OUT/diskheat1.png")
height, width, _ = img.shape
for y in range(1, height):
    for x in range(1, width):
        (b, g, r) = img[y, x]
        if b > 110:
            img[y, x] = (255, 255, 255)
        else:
            img[y, x] = (0, 0, 0)
im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create(params)

im = im[1:height, 1:width]
row, col = im.shape[:2]
bottom = im[row - 2:row, 0:col]
mean = cv2.mean(bottom)[0]

bordersize = 50
border = cv2.copyMakeBorder(
    im,
    top=bordersize,
    bottom=bordersize,
    left=bordersize,
    right=bordersize,
    borderType=cv2.BORDER_CONSTANT,
    value=[255, 255, 255]
)

# Detect blobs.
keypoints = detector.detect(border)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(border, keypoints, np.array([]), (0, 255, 0),
                                      cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)  # DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS
n = 0
pixel_len_meter = math.sqrt(single_pxl_area/ 1000000)
print(pixel_len_meter)
HexagonExtraction.markHexagoninImg(color_img)
color_img = cv2.imread("HEAT_IMG/OUT/bgremoved.png", cv2.IMREAD_UNCHANGED)
while n < len(keypoints):
    print(keypoints[n].size)
    area = int((math.pi * (keypoints[n].size / 2) ** 2) * single_pxl_area) / 10000
    side = 1.5 * keypoints[n].size
    cx = int(keypoints[n].pt[0]) - 50
    cy = int(keypoints[n].pt[1]) - 50

    res_lat, res_long = GPSCoordinates.getCordinatesFromCenter(pixel_len_meter, lat, long, cx, cy, int(width / 2),
                                                               int(height / 2))
    print(res_lat, res_long, area)
    cv2.rectangle(color_img, pt1=(int(cx - side / 2), int(cy - side / 2)), pt2=(int(cx + side / 2), int(cy + side / 2)),
                  color=[255, 255, 255, 255], thickness=3)
    cv2.putText(color_img, str(round(area, 3)) + " m.sq", (int(cx - side / 2), cy - int(side / 1.8)), cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255, 255), 2)
    cv2.putText(color_img, str(round(res_lat, 7)) + ", " + str(round(res_long, 7)), (int(cx - side), cy - int(side / 1.8) - 35),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                (255, 255, 255, 255), 2)
    cv2.putText(color_img, ".",  (int(width/2), int(height/2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255,255), 5)
    cv2.putText(color_img, "Sprinkler", (int(width/2) - 100, int(height/2) - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255,255), 2)

    n = n + 1
cv2.imwrite('HEAT_IMG/OUT/BlobFinal.png', color_img)
cv2.imshow('border', color_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
