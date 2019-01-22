import numpy

# pip install numpy
# pip install opencv-python
# pip install ipython

# Numpy is a base library for other libraries like pandas and open cv, an image processing library

# ----------- One Dimension Array--------------------
oneDi = numpy.arange(27)
print(oneDi)
# outputs:
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])

# ----------- Two Dimensional Array------------------
twoDi = oneDi.reshape(3, 9)  # makes two dimensional array 3 by 9
print(twoDi)
# outputs:
# [[ 0  1  2  3  4  5  6  7  8]
#  [ 9 10 11 12 13 14 15 16 17]
#  [18 19 20 21 22 23 24 25 26]]

# ----------- Three Dimensional Array------------------
threeDi = oneDi.reshape(3, 3, 3)  # three dimensional array 3 by 3 by 3
print(threeDi)
# outputs:
# [[[ 0  1  2]
#   [ 3  4  5]
#   [ 6  7  8]]

#  [[ 9 10 11]
#   [12 13 14]
#   [15 16 17]]

#  [[18 19 20]
#   [21 22 23]
#   [24 25 26]]]

