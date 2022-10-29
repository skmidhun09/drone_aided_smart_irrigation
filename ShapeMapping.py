import cv2
import glob
from xlwt import Workbook

def processImage(imageName , totalImageCount):
    img = cv2.imread(imageName)
    height, width = img.shape
    print(height, "sample", width)

processImage("HEAT_IMG/OUT/heat.png",1)