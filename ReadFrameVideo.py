import cv2
import numpy as np

vidcap = cv2.VideoCapture('Output/result2.avi')
success, image = vidcap.read()
fps, frames = vidcap.get(cv2.CAP_PROP_FPS), vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
count = 0
height, width, _ = image.shape
x, y, h, w = 0, 0, height, width
while success:
    # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

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
    imgZoom = cv2.resize(red_img, (4 * width, 4 * height))
    cv2.imshow("Output", imgZoom)
    cv2.waitKey(20)
    # cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
    success, image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('Output/grey_video.avi', fourcc, fps, (w, h))
    out.write(image)
