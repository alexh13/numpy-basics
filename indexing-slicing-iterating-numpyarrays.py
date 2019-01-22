import numpy
import cv2
# pip install numpy
# pip install opencv-python
# pip install ipython

# ------------------- Indexing ---------------------------
im_g = cv2.imread("smallgray.png", 0)  # load image to get numpy array
print(im_g)
# outputs:
# [[187 158 104 121 143]
#  [198 125 255 255 147]
#  [209 134 255  97 182]]
# i want to get 104, 121, 255 and 255

print(im_g[0:2, 2:4])  # gives the first two rows then after the comma is the index for the columns
# outputs:
# [[104 121]
#  [255 255]]

print(im_g.shape)  # gives shape of array
# outputs (3, 5)

# ------------------- Iterating ---------------------------
for i in im_g:  # i accesses the rows
    print(i)
# outputs:
# [187 158 104 121 143]
# [198 125 255 255 147]
# [209 134 255  97 182]

for i in im_g.T:  # i accesses the columns you the transpose method
    print(i)
# outputs:
# [187 198 209]
# [158 125 134]
# [104 255 255]
# [121 255  97]
# [143 147 182]

for i in im_g.flat:  # access values of array one by one
    print(i)
# outputs:
# 187
# 158
# 104
# 121
# 143
# 198
# 125
# 255
# 255
# 147
# 209
# 134
# 255
# 97
# 182
