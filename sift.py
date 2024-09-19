import cv2
import matplotlib.pyplot as plt
import numpy as np

image1 = cv2.imread(r'/home/isaac/Desktop/pcv/pcv_lab/test.webp')

if image1 is None:
    print('Could not open or find the image')
    exit(0)
else:
    training_image = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

    training_gray = cv2.cvtColor(training_image, cv2.COLOR_RGB2GRAY)

    test_image = cv2.pyrDown(training_image)

    test_image = cv2.pyrDown(test_image)

    num_rows, num_cols = test_image.shape[:2]

    rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), 30, 1)

    test_image = cv2.warpAffine(test_image, rotation_matrix, (num_cols, num_rows))

    test_gray = cv2.cvtColor(test_image, cv2.COLOR_RGB2GRAY)

    fig, plots = plt.subplots(1, 2, figsize = (20,10))


    #SIFT

    sift = cv2.SIFT_create()

    keypoints_train, descriptors_train = sift.detectAndCompute(training_gray, None)
    keypoints_test, descriptors_train = sift.detectAndCompute(test_gray, None)

    training_image_with_keypoints = cv2.drawKeypoints(training_image, keypoints_train, None)
    test_image_with_keypoints = cv2.drawKeypoints(test_image, keypoints_test, None)

    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck = False)

    matches = bf.match(descriptors_train, descriptors_train)
    matches = sorted(matches, key=lambda x:x.distance)

    result = cv2.drawMatches(training_image, keypoints_train, test_image, keypoints_test, matches[:50],
    None, flags = cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    plt.figure(figsize = (14,7))

    plt.title('Best Matching Points') 

    plt.imshow(result) 
    plt.axis('off')  # Hide axes for better visualization 
    plt.show() 
    print("\nNumber of Matching Keypoints Between The Training and Query Images: ", len(matches)) 


  