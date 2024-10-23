import numpy as np
import cv2 as cv

img = cv.imread(r'/home/isaac/Desktop/pcv/pcv_lab/images.jpeg', 0)

rows, cols = img.shape

img_shrinked = cv.resize(img, (rows, cols), interpolation=cv.INTER_AREA)

cv.imshow('shrinked', img_shrinked)

img_enlarged = cv.resize(img_shrinked, None, fx=1.5, fy=1.5, interpolation = cv.INTER_CUBIC)

cv.imshow('enlarged', img_enlarged)

cv.waitKey(0)

cv.destroyAllWindows()


