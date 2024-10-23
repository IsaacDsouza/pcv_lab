import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'/home/isaac/Desktop/pcv/pcv_lab/images.jpeg')

image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

plt.figure(figsize=(10, 10))

plt.subplot(221)

plt.imshow(image)

img_hist = cv2.calcHist([gray], [0], None, [256], [0,256])

plt.subplot(222)

plt.plot(img_hist)

plt.subplot(223) 

plt.hist(gray.ravel(), 256, [0, 256]) 

plt.title('Histogram using ravel()') 

equalized = cv2.equalizeHist(gray)

plt.subplot(224)

plt.imshow(equalized, cmap='gray')

plt.show()