import cv2
import glob
from xlwt import Workbook

# Workbook is created
wb = Workbook()
row = 1
sheet1 = wb.add_sheet('PixelData')
sheet1.write(0, 0, 'IMAGE')
sheet1.write(0, 1, 'COUNT')

def addtoExcel(imgName, count):
    global row
    sheet1.write(row, 0, imgName)
    sheet1.write(row, 1, count)
    wb.save('HEAT_IMG\OUT\pixel_count.xls')
    row = row + 1


def processImage(imageName , totalImageCount):
    print("sample height:")
    img = cv2.imread(imageName)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width = gray_image.shape
    print(height, "sample", width)
    #cv2.imshow('Grayscale', gray_image)
    #cv2.waitKey(0)
    count = 0
    correction = 8
    cheight = int(height/correction)
    cwidth = int(width/correction)
    height = height - cheight
    width = width - cwidth
    print(height, width)
    updatedName = imageName.rsplit('\\', 1)[1]
    cv2.imwrite('HEAT_IMG/MID/' + updatedName, gray_image)
    for y in range(cheight, height):
        for x in range(cwidth, width):
            pixel = gray_image[y, x]
            if pixel <= 160:
                count += 1
                gray_image[y, x] = 0
    cv2.imwrite('HEAT_IMG/OUT/' + updatedName, gray_image)
    print(updatedName, " count= ",count)
    addtoExcel(updatedName, count)
    #cv2.imshow('Grayscale', gray_image)
    #cv2.waitKey(0)
    cv2.destroyAllWindows()

def bulkImageProcess(imgPath):
    images = glob.glob(imgPath)
    for image in images:
        processImage(image, len(images))

bulkImageProcess("HEAT_IMG/IN/*")