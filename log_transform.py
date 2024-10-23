import cv2
import numpy as np

# Load the image
img = cv2.imread(r'/home/isaac/Desktop/pcv/pcv_lab/images.jpeg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Set the constants
gamma = 1.5
c = 20

# Apply logarithmic transformation
log_img = c * np.log(1 + gray.astype(np.float64))

# Normalize the result to fit into the 8-bit range (0-255)
log_img = cv2.normalize(log_img, None, 0, 255, cv2.NORM_MINMAX)

# Convert the result back to an unsigned 8-bit integer type for display
log_img = np.uint8(log_img)

# Concatenate the original grayscale image and the log-transformed image
res = cv2.hconcat([gray, log_img])

# Display the images
cv2.imshow('images', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
