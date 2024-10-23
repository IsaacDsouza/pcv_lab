import cv2 
import numpy as np


img = cv2.imread(r'/home/isaac/Desktop/pcv/pcv_lab/images.jpeg',0)

row, column = img.shape

img_array = np.zeros((row, column), dtype='uint8')

min_range = 100
max_range = 200

for i in range(row):
    for j in range(column):
        if img[i,j] > min_range and img[i,j] < max_range:
            img_array[i,j] = 255
        else:
            if i>0 and j>0:
                img_array[i, j] = img[i-1, j-1]
            else:
                img_array[i,j] = 0


cv2.imwrite("gray_slicing.jpg", img_array)

cv2.imshow("Gray Slicing", img_array)
cv2.imshow("Original Image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()
