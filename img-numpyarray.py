import numpy
import cv2
# pip install numpy
# pip install opencv-python
# pip install ipython


# ------------- Creating images to numpy arrays ------------------------------
im_g = cv2.imread("smallgray.png", 0)  # load image into python using image read method. 0 is gray scale, 1 is BGR
print(im_g)
# outputs:
# [[187 158 104 121 143]
#  [198 125 255 255 147]
#  [209 134 255  97 182]]
# the numbers are the color values per pixel ranging from 0-255


# ------------- Creating numpy arrays to images ------------------------------
cv2.imwrite("newsmallgray.png", im_g)
# use the imwrite method to write an image
# after imwrite declare name for image followed by a , and the array you want to convert

