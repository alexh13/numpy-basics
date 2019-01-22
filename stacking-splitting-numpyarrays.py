import numpy
import cv2
# pip install numpy
# pip install opencv-python
# pip install ipython

im_g = cv2.imread("smallgray.png", 0)  # load image to get numpy array
print(im_g)
# outputs:
# [[187 158 104 121 143]
#  [198 125 255 255 147]
#  [209 134 255  97 182]]

# ------------------ Concatenating (stacking) Arrays --------------------------- #
ims = numpy.hstack((im_g, im_g))  # horizontal stack expects 2 or more numpy arrays to concatenate, must be a tuple
print(ims)
# outputs:
# [[187 158 104 121 143 187 158 104 121 143]
#  [198 125 255 255 147 198 125 255 255 147]
#  [209 134 255  97 182 209 134 255  97 182]]

ims = numpy.vstack((im_g, im_g))  # vertically stack arrays
print(ims)
# outputs:
# [[187 158 104 121 143]
#  [198 125 255 255 147]
#  [209 134 255  97 182]
#  [187 158 104 121 143]
#  [198 125 255 255 147]
#  [209 134 255  97 182]]

# ------------------ Splitting Arrays --------------------------- #
lst = numpy.hsplit(im_g, 5)  # horizontally split array by 5
print(lst)
# outputs:
# [array([[187],
#        [198],
#        [209]], dtype=uint8), array([[158],
#        [125],
#        [134]], dtype=uint8), array([[104],
#        [255],
#        [255]], dtype=uint8), array([[121],
#        [255],
#        [ 97]], dtype=uint8), array([[143],
#        [147],
#        [182]], dtype=uint8)]

lst = numpy.vsplit(im_g, 3)  # vertically split array by 3
print(lst)
# outputs:
# [array([[187, 158, 104, 121, 143]], dtype=uint8),
# array([[198, 125, 255, 255, 147]], dtype=uint8),
# array([[209, 134, 255,  97, 182]], dtype=uint8)]





