import cv2

def find_area():
    img = cv2.imread("HEAT_IMG/OUT/Area.png")
    height, width, _ = img.shape
    count_a_dash = 0
    count_a = 0
    for y in range(1, height):
        for x in range(1, width):
            (b, g, r) = img[y, x]
            if r == 0:
                count_a_dash= count_a_dash + 1
                img[y, x] = 255,255,255
            else:
                count_a = count_a + 1
    print("A dash:",count_a_dash, " Area: ",count_a)
    cv2.imshow("Output", img)
    cv2.waitKey(5000)


find_area()