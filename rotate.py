import cv2  

# Read the input image  

img = cv2.imread(r'/home/isaac/Desktop/pcv/pcv_lab/images.jpeg')  

# Define the rotation angle  

angle = 45  

# Get the image dimensions  
h, w = img.shape[:2]  

# Calculate the rotation matrix M  

M = cv2.getRotationMatrix2D((w/2, h/2), angle, 1) 

# Apply the rotation to the image  

rotated_img = cv2.warpAffine(img, M, (w, h))  

cv2.imshow('Original Image', img)  

cv2.imshow('Rotated Image', rotated_img)  

cv2.waitKey(0)  

# Release the memory and destroy all windows  

cv2.destroyAllWindows() 