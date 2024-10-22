import cv2

img = cv2.imread(r'/home/isaac/Desktop/pcv/pcv_lab/images.jpeg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

neg = cv2.bitwise_not(gray)

cv2.imshow('image', neg)

key = cv2.waitKey(0)


cv2.destroyAllWindows()