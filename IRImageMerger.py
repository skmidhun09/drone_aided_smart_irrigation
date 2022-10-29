# Import statements
import cv2
import numpy as np
# Open the images
rgb = cv2.imread(‘RGB.png’)
ir = cv2.imread(‘IR.png’)
# Create a mask based on the Laplace operator
mask = cv2.Laplacian(rgb, cv2.CV_8U, ksize=3)
# Invert the mask (black to white, white to black)
mask_inv = cv2.bitwise_not(mask)
# Add the edges on top of the IR image
ir_enhanced = cv2.add(ir, mask)
# Add the edges on top of the IR image
ir_enhanced_inv = cv2.bitwise_and(ir, mask_inv)