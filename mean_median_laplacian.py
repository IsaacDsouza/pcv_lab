import cv2

import numpy as np

img = cv2.imread(r'/home/isaac/Desktop/pcv/pcv_lab/images.jpeg')

kernel = np.ones((5,5), np.float32)/25

mean_filtered = cv2.filter2D(img, -1, kernel)

median_filtered = cv2.medianBlur(img, 5)

sharpened_image = cv2.Laplacian(img, cv2.CV_64F)

sharpened_image = np.uint8(np.absolute(sharpened_image))

cv2.imshow("mean", mean_filtered)
cv2.imshow("median", median_filtered)
cv2.imshow("Laplacian", sharpened_image)

cv2.waitKey(0)

cv2.destroyAllwindows()