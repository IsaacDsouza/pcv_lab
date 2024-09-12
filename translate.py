import numpy as np 
import cv2 as cv

img = cv.imread(r'/home/isaac/Desktop/pcv/pcv_lab/images.jpeg', 0)

rows, cols = img.shape

M = np.float32([[1, 0, 100],[0, 1, 50]])

dst = cv.warpAffine(img, M, (cols, rows))

cv.imshow('image', dst)

cv.waitKey(0)

cv.destroyAllWindows()