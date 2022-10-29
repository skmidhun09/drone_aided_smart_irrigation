import math
import cv2
from PIL import Image
import GPSCoordinates


def drawaxis():
    cv2.arrowedLine(img, (0, height - 14), (width - 3, height - 14), color=write_clr, thickness=3, tipLength=0.015)
    cv2.putText(img, "Height=" + str(real_h) + "m", (24, int(height / 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, write_clr, 2)
    cv2.arrowedLine(img, (14, width), (14, 3), color=write_clr, thickness=3, tipLength=0.015)
    cv2.putText(img, "Width=" + str(real_w) + "m", (int(width * 2 / 5), height - 24), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                write_clr, 2)


write_clr = (255, 255, 255)
zoom_ratio = 8
known_area = 1600
input_image = "HEAT_IMG/OUT/Area1.png"
output_image = "HEAT_IMG/OUT/diskheat1.png"
image_file = Image.open(input_image)
h, w = image_file.size
size = h * zoom_ratio, w * zoom_ratio
im_resized = image_file.resize(size, Image.ANTIALIAS)
im_resized.save(output_image, "PNG")
img = cv2.imread(output_image)
height, width, _ = img.shape
xc = int(width / 2)
yc = int(height / 2)
count_a_dash = 0
count_a = 0
first_value = True
init_x = width
init_y = 0
final_x = 0
final_y = 0
for y in range(1, height):
    for x in range(1, width):
        (b, g, r) = img[y, x]
        if b == 0:
            count_a_dash = count_a_dash + 1
            if x < init_x:
                init_x = x
            if x > final_x:
                final_x = x
            if first_value:
                init_y = y
                first_value = False
            final_y = y
        else:
            count_a = count_a + 1

cv2.rectangle(img, pt1=(init_x - int((final_x - init_x) / 4), init_y - int((final_y - init_y) / 4)),
              pt2=(final_x + int((final_x - init_x) / 4), final_y + int((final_y - init_y) / 4)), color=write_clr,
              thickness=3)
rect_xc = final_x - int((final_x - init_x) / 2)
rect_yc = final_y - int((final_y - init_y) / 2)
cv2.putText(img, 'Area=' + str(known_area) + "cm.sq",
            (init_x - int((final_x - init_x)), init_y - int((final_y - init_y) / 4) - 10), cv2.FONT_HERSHEY_SIMPLEX,
            0.9, write_clr, 2)
unit_pixel_area = known_area / count_a_dash
unit_side = math.sqrt(unit_pixel_area)
real_h = int(unit_side * height) / 100
real_w = int(unit_side * width) / 100
total_area = int(unit_side * height * unit_side * width) / 10000
# drawaxis()
# cv2.putText(img, "Area=" + str(total_area) + "m.sq", (int(width * 2 / 5), 24), cv2.FONT_HERSHEY_DUPLEX, 0.9, write_clr,2)
print(real_h * real_w)

if rect_xc > xc:
    if rect_yc >= yc:
        quadrant = 1
    else:
        quadrant = 4
else:
    if rect_yc >= yc:
        quadrant = 2
    else:
        quadrant = 3

lat = 36.8490881
long = -76.2544901
resp_lat, resp_long = GPSCoordinates.getCordinates(lat, long, rect_xc, rect_yc, quadrant)
cv2.putText(img, ".", (xc, yc), cv2.FONT_HERSHEY_SIMPLEX, 1, write_clr, 5)
cv2.putText(img, "Sprinkler", (xc, yc + 28), cv2.FONT_HERSHEY_SIMPLEX, 0.8, write_clr, 2)
cv2.putText(img, str(round(resp_lat, 7)) + ',',
            (init_x - int((final_x - init_x)), final_y + int((final_y - init_y) / 2)),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, write_clr, 2)
cv2.putText(img, str(round(resp_long, 7)),
            (init_x - int((final_x - init_x)), final_y + int((final_y - init_y) / 2 + 29)),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, write_clr, 2)
cv2.imwrite('HEAT_IMG/OUT/dimension1.png', img)
cv2.imshow('Grayscale', img)
cv2.waitKey(5000)
